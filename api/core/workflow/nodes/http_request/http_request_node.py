import logging
from mimetypes import guess_extension
from os import path
from typing import cast

from core.app.segments import parser
from core.file.file_obj import FileTransferMethod, FileType, FileVar
from core.tools.tool_file_manager import ToolFileManager
from core.workflow.entities.base_node_data_entities import BaseNodeData
from core.workflow.entities.node_entities import NodeRunResult, NodeType
from core.workflow.entities.variable_pool import VariablePool
from core.workflow.nodes.base_node import BaseNode
from core.workflow.nodes.http_request.entities import (
    MAX_CONNECT_TIMEOUT,
    MAX_READ_TIMEOUT,
    MAX_WRITE_TIMEOUT,
    HttpRequestNodeData,
    HttpRequestNodeTimeout,
)
from core.workflow.nodes.http_request.http_executor import HttpExecutor, HttpExecutorResponse
from models.workflow import WorkflowNodeExecutionStatus

HTTP_REQUEST_DEFAULT_TIMEOUT = HttpRequestNodeTimeout(
    connect=min(10, MAX_CONNECT_TIMEOUT),
    read=min(60, MAX_READ_TIMEOUT),
    write=min(20, MAX_WRITE_TIMEOUT),
)


class HttpRequestNode(BaseNode):
    _node_data_cls = HttpRequestNodeData
    _node_type = NodeType.HTTP_REQUEST

    @classmethod
    def get_default_config(cls, filters: dict | None = None) -> dict:
        return {
            'type': 'http-request',
            'config': {
                'method': 'get',
                'authorization': {
                    'type': 'no-auth',
                },
                'body': {'type': 'none'},
                'timeout': {
                    **HTTP_REQUEST_DEFAULT_TIMEOUT.model_dump(),
                    'max_connect_timeout': MAX_CONNECT_TIMEOUT,
                    'max_read_timeout': MAX_READ_TIMEOUT,
                    'max_write_timeout': MAX_WRITE_TIMEOUT,
                },
            },
        }

    def _run(self, variable_pool: VariablePool) -> NodeRunResult:
        node_data: HttpRequestNodeData = cast(HttpRequestNodeData, self.node_data)
        # TODO: Switch to use segment directly
        if node_data.authorization.config and node_data.authorization.config.api_key:
            node_data.authorization.config.api_key = parser.convert_template(template=node_data.authorization.config.api_key, variable_pool=variable_pool).text

        # init http executor
        http_executor = None
        try:
            http_executor = HttpExecutor(
                node_data=node_data, timeout=self._get_request_timeout(node_data), variable_pool=variable_pool
            )

            # invoke http executor
            response = http_executor.invoke()
        except Exception as e:
            process_data = {}
            if http_executor:
                process_data = {
                    'request': http_executor.to_raw_request(),
                }
            return NodeRunResult(
                status=WorkflowNodeExecutionStatus.FAILED,
                error=str(e),
                process_data=process_data,
            )

        files = self.extract_files(http_executor.server_url, response)

        return NodeRunResult(
            status=WorkflowNodeExecutionStatus.SUCCEEDED,
            outputs={
                'status_code': response.status_code,
                'body': response.content if not files else '',
                'headers': response.headers,
                'files': files,
            },
            process_data={
                'request': http_executor.to_raw_request(),
            },
        )

    def _get_request_timeout(self, node_data: HttpRequestNodeData) -> HttpRequestNodeTimeout:
        timeout = node_data.timeout
        if timeout is None:
            return HTTP_REQUEST_DEFAULT_TIMEOUT

        timeout.connect = timeout.connect or HTTP_REQUEST_DEFAULT_TIMEOUT.connect
        timeout.connect = min(timeout.connect, MAX_CONNECT_TIMEOUT)
        timeout.read = timeout.read or HTTP_REQUEST_DEFAULT_TIMEOUT.read
        timeout.read = min(timeout.read, MAX_READ_TIMEOUT)
        timeout.write = timeout.write or HTTP_REQUEST_DEFAULT_TIMEOUT.write
        timeout.write = min(timeout.write, MAX_WRITE_TIMEOUT)
        return timeout

    @classmethod
    def _extract_variable_selector_to_variable_mapping(cls, node_data: BaseNodeData) -> dict[str, list[str]]:
        """
        Extract variable selector to variable mapping
        :param node_data: node data
        :return:
        """
        node_data = cast(HttpRequestNodeData, node_data)
        try:
            http_executor = HttpExecutor(node_data=node_data, timeout=HTTP_REQUEST_DEFAULT_TIMEOUT)

            variable_selectors = http_executor.variable_selectors

            variable_mapping = {}
            for variable_selector in variable_selectors:
                variable_mapping[variable_selector.variable] = variable_selector.value_selector

            return variable_mapping
        except Exception as e:
            logging.exception(f'Failed to extract variable selector to variable mapping: {e}')
            return {}

    def extract_files(self, url: str, response: HttpExecutorResponse) -> list[FileVar]:
        """
        Extract files from response
        """
        files = []
        mimetype, file_binary = response.extract_file()

        if mimetype:
            # extract filename from url
            filename = path.basename(url)
            # extract extension if possible
            extension = guess_extension(mimetype) or '.bin'

            tool_file = ToolFileManager.create_file_by_raw(
                user_id=self.user_id,
                tenant_id=self.tenant_id,
                conversation_id=None,
                file_binary=file_binary,
                mimetype=mimetype,
            )

            files.append(
                FileVar(
                    tenant_id=self.tenant_id,
                    type=FileType.IMAGE,
                    transfer_method=FileTransferMethod.TOOL_FILE,
                    related_id=tool_file.id,
                    filename=filename,
                    extension=extension,
                    mime_type=mimetype,
                )
            )

        return files
