import time
import uuid
from urllib.parse import urlencode

import pytest

from core.app.entities.app_invoke_entities import InvokeFrom
from core.workflow.entities.node_entities import UserFrom
from core.workflow.entities.variable_pool import VariablePool
from core.workflow.enums import SystemVariableKey
from core.workflow.graph_engine.entities.graph import Graph
from core.workflow.graph_engine.entities.graph_init_params import GraphInitParams
from core.workflow.graph_engine.entities.graph_runtime_state import GraphRuntimeState
from core.workflow.nodes.http_request.http_request_node import HttpRequestNode
from models.workflow import WorkflowType
from tests.integration_tests.workflow.nodes.__mock.http import setup_http_mock


def init_http_node(config: dict):
    graph_config = {
        "edges": [
            {
                "id": "start-source-next-target",
                "source": "start",
                "target": "1",
            },
        ],
        "nodes": [{"data": {"type": "start"}, "id": "start"}, config],
    }

    graph = Graph.init(graph_config=graph_config)

    init_params = GraphInitParams(
        tenant_id="1",
        app_id="1",
        workflow_type=WorkflowType.WORKFLOW,
        workflow_id="1",
        graph_config=graph_config,
        user_id="1",
        user_from=UserFrom.ACCOUNT,
        invoke_from=InvokeFrom.DEBUGGER,
        call_depth=0,
    )

    # construct variable pool
    variable_pool = VariablePool(
        system_variables={SystemVariableKey.FILES: [], SystemVariableKey.USER_ID: "aaa"},
        user_inputs={},
        environment_variables=[],
        conversation_variables=[],
    )
    variable_pool.add(["a", "b123", "args1"], 1)
    variable_pool.add(["a", "b123", "args2"], 2)

    return HttpRequestNode(
        id=str(uuid.uuid4()),
        graph_init_params=init_params,
        graph=graph,
        graph_runtime_state=GraphRuntimeState(variable_pool=variable_pool, start_at=time.perf_counter()),
        config=config,
    )


@pytest.mark.parametrize("setup_http_mock", [["none"]], indirect=True)
def test_get(setup_http_mock):
    node = init_http_node(
        config={
            "id": "1",
            "data": {
                "title": "http",
                "desc": "",
                "method": "get",
                "url": "http://example.com",
                "authorization": {
                    "type": "api-key",
                    "config": {
                        "type": "basic",
                        "api_key": "ak-xxx",
                        "header": "api-key",
                    },
                },
                "headers": "X-Header:123",
                "params": "A:b",
                "body": None,
            },
        }
    )

    result = node._run()
    assert result.process_data is not None
    data = result.process_data.get("request", "")

    assert "?A=b" in data
    assert "X-Header: 123" in data


@pytest.mark.parametrize("setup_http_mock", [["none"]], indirect=True)
def test_no_auth(setup_http_mock):
    node = init_http_node(
        config={
            "id": "1",
            "data": {
                "title": "http",
                "desc": "",
                "method": "get",
                "url": "http://example.com",
                "authorization": {
                    "type": "no-auth",
                    "config": None,
                },
                "headers": "X-Header:123",
                "params": "A:b",
                "body": None,
            },
        }
    )

    result = node._run()
    assert result.process_data is not None
    data = result.process_data.get("request", "")

    assert "?A=b" in data
    assert "X-Header: 123" in data


@pytest.mark.parametrize("setup_http_mock", [["none"]], indirect=True)
def test_custom_authorization_header(setup_http_mock):
    node = init_http_node(
        config={
            "id": "1",
            "data": {
                "title": "http",
                "desc": "",
                "method": "get",
                "url": "http://example.com",
                "authorization": {
                    "type": "api-key",
                    "config": {
                        "type": "custom",
                        "api_key": "Auth",
                        "header": "X-Auth",
                    },
                },
                "headers": "X-Header:123",
                "params": "A:b",
                "body": None,
            },
        }
    )

    result = node._run()
    assert result.process_data is not None
    data = result.process_data.get("request", "")

    assert "?A=b" in data
    assert "X-Header: 123" in data


@pytest.mark.parametrize("setup_http_mock", [["none"]], indirect=True)
def test_template(setup_http_mock):
    node = init_http_node(
        config={
            "id": "1",
            "data": {
                "title": "http",
                "desc": "",
                "method": "get",
                "url": "http://example.com/{{#a.b123.args2#}}",
                "authorization": {
                    "type": "api-key",
                    "config": {
                        "type": "basic",
                        "api_key": "ak-xxx",
                        "header": "api-key",
                    },
                },
                "headers": "X-Header:123\nX-Header2:{{#a.b123.args2#}}",
                "params": "A:b\nTemplate:{{#a.b123.args2#}}",
                "body": None,
            },
        }
    )

    result = node._run()
    assert result.process_data is not None
    data = result.process_data.get("request", "")

    assert "?A=b" in data
    assert "Template=2" in data
    assert "X-Header: 123" in data
    assert "X-Header2: 2" in data


@pytest.mark.parametrize("setup_http_mock", [["none"]], indirect=True)
def test_json(setup_http_mock):
    node = init_http_node(
        config={
            "id": "1",
            "data": {
                "title": "http",
                "desc": "",
                "method": "post",
                "url": "http://example.com",
                "authorization": {
                    "type": "api-key",
                    "config": {
                        "type": "basic",
                        "api_key": "ak-xxx",
                        "header": "api-key",
                    },
                },
                "headers": "X-Header:123",
                "params": "A:b",
                "body": {"type": "json", "data": '{"a": "{{#a.b123.args1#}}"}'},
            },
        }
    )

    result = node._run()
    assert result.process_data is not None
    data = result.process_data.get("request", "")

    assert '{"a": "1"}' in data
    assert "X-Header: 123" in data


def test_x_www_form_urlencoded(setup_http_mock):
    node = init_http_node(
        config={
            "id": "1",
            "data": {
                "title": "http",
                "desc": "",
                "method": "post",
                "url": "http://example.com",
                "authorization": {
                    "type": "api-key",
                    "config": {
                        "type": "basic",
                        "api_key": "ak-xxx",
                        "header": "api-key",
                    },
                },
                "headers": "X-Header:123",
                "params": "A:b",
                "body": {"type": "x-www-form-urlencoded", "data": "a:{{#a.b123.args1#}}\nb:{{#a.b123.args2#}}"},
            },
        }
    )

    result = node._run()
    assert result.process_data is not None
    data = result.process_data.get("request", "")

    assert "a=1&b=2" in data
    assert "X-Header: 123" in data


def test_form_data(setup_http_mock):
    node = init_http_node(
        config={
            "id": "1",
            "data": {
                "title": "http",
                "desc": "",
                "method": "post",
                "url": "http://example.com",
                "authorization": {
                    "type": "api-key",
                    "config": {
                        "type": "basic",
                        "api_key": "ak-xxx",
                        "header": "api-key",
                    },
                },
                "headers": "X-Header:123",
                "params": "A:b",
                "body": {"type": "form-data", "data": "a:{{#a.b123.args1#}}\nb:{{#a.b123.args2#}}"},
            },
        }
    )

    result = node._run()
    assert result.process_data is not None
    data = result.process_data.get("request", "")

    assert 'form-data; name="a"' in data
    assert "1" in data
    assert 'form-data; name="b"' in data
    assert "2" in data
    assert "X-Header: 123" in data


def test_none_data(setup_http_mock):
    node = init_http_node(
        config={
            "id": "1",
            "data": {
                "title": "http",
                "desc": "",
                "method": "post",
                "url": "http://example.com",
                "authorization": {
                    "type": "api-key",
                    "config": {
                        "type": "basic",
                        "api_key": "ak-xxx",
                        "header": "api-key",
                    },
                },
                "headers": "X-Header:123",
                "params": "A:b",
                "body": {"type": "none", "data": "123123123"},
            },
        }
    )

    result = node._run()
    assert result.process_data is not None
    data = result.process_data.get("request", "")

    assert "X-Header: 123" in data
    assert "123123123" not in data


def test_mock_404(setup_http_mock):
    node = init_http_node(
        config={
            "id": "1",
            "data": {
                "title": "http",
                "desc": "",
                "method": "get",
                "url": "http://404.com",
                "authorization": {
                    "type": "no-auth",
                    "config": None,
                },
                "body": None,
                "params": "",
                "headers": "X-Header:123",
            },
        }
    )

    result = node._run()
    assert result.outputs is not None
    resp = result.outputs

    assert 404 == resp.get("status_code")
    assert "Not Found" in resp.get("body", "")


def test_multi_colons_parse(setup_http_mock):
    node = init_http_node(
        config={
            "id": "1",
            "data": {
                "title": "http",
                "desc": "",
                "method": "get",
                "url": "http://example.com",
                "authorization": {
                    "type": "no-auth",
                    "config": None,
                },
                "params": "Referer:http://example1.com\nRedirect:http://example2.com",
                "headers": "Referer:http://example3.com\nRedirect:http://example4.com",
                "body": {"type": "form-data", "data": "Referer:http://example5.com\nRedirect:http://example6.com"},
            },
        }
    )

    result = node._run()
    assert result.process_data is not None
    assert result.outputs is not None
    resp = result.outputs

    assert urlencode({"Redirect": "http://example2.com"}) in result.process_data.get("request", "")
    assert 'form-data; name="Redirect"\n\nhttp://example6.com' in result.process_data.get("request", "")
    assert "http://example3.com" == resp.get("headers", {}).get("referer")
