from collections.abc import Sequence
from typing import Optional, cast

from core.workflow.entities.base_node_data_entities import BaseNodeData
from core.workflow.entities.node_entities import NodeRunResult, NodeType
from core.workflow.entities.variable_pool import VariablePool
from core.workflow.nodes.base_node import BaseNode
from core.workflow.nodes.if_else.entities import Condition, IfElseNodeData
from core.workflow.utils.variable_template_parser import VariableTemplateParser
from models.workflow import WorkflowNodeExecutionStatus


class IfElseNode(BaseNode):
    _node_data_cls = IfElseNodeData
    _node_type = NodeType.IF_ELSE

    def _run(self, variable_pool: VariablePool) -> NodeRunResult:
        """
        Run node
        :param variable_pool: variable pool
        :return:
        """
        node_data = self.node_data
        node_data = cast(IfElseNodeData, node_data)

        node_inputs = {
            "conditions": []
        }

        process_datas = {
            "condition_results": []
        }

        input_conditions = []
        final_result = False
        selected_case_id = None
        try:
            # Check if the new cases structure is used
            if node_data.cases:
                for case in node_data.cases:
                    input_conditions, group_result = self.process_conditions(variable_pool, case.conditions)
                    # Apply the logical operator for the current case
                    final_result = all(group_result) if case.logical_operator == "and" else any(group_result)

                    process_datas["condition_results"].append(
                        {
                            "group": case.model_dump(),
                            "results": group_result,
                            "final_result": final_result,
                        }
                    )

                    # Break if a case passes (logical short-circuit)
                    if final_result:
                        selected_case_id = case.case_id  # Capture the ID of the passing case
                        break

            else:
                # Fallback to old structure if cases are not defined
                input_conditions, group_result = self.process_conditions(variable_pool, node_data.conditions)

                final_result = all(group_result) if node_data.logical_operator == "and" else any(group_result)

                selected_case_id = "true" if final_result else "false"

                process_datas["condition_results"].append(
                    {
                        "group": "default",
                        "results": group_result,
                        "final_result": final_result
                    }
                )

            node_inputs["conditions"] = input_conditions

        except Exception as e:
            return NodeRunResult(
                status=WorkflowNodeExecutionStatus.FAILED,
                inputs=node_inputs,
                process_data=process_datas,
                error=str(e)
            )

        outputs = {"result": final_result, "selected_case_id": selected_case_id}

        data = NodeRunResult(
            status=WorkflowNodeExecutionStatus.SUCCEEDED,
            inputs=node_inputs,
            process_data=process_datas,
            edge_source_handle=selected_case_id if selected_case_id else "false",  # Use case ID or 'default'
            outputs=outputs
        )

        return data

    def evaluate_condition(
        self, actual_value: Optional[str | list], expected_value: str, comparison_operator: str
    ) -> bool:
        """
        Evaluate condition
        :param actual_value: actual value
        :param expected_value: expected value
        :param comparison_operator: comparison operator

        :return: bool
        """
        if comparison_operator == "contains":
            return self._assert_contains(actual_value, expected_value)
        elif comparison_operator == "not contains":
            return self._assert_not_contains(actual_value, expected_value)
        elif comparison_operator == "start with":
            return self._assert_start_with(actual_value, expected_value)
        elif comparison_operator == "end with":
            return self._assert_end_with(actual_value, expected_value)
        elif comparison_operator == "is":
            return self._assert_is(actual_value, expected_value)
        elif comparison_operator == "is not":
            return self._assert_is_not(actual_value, expected_value)
        elif comparison_operator == "empty":
            return self._assert_empty(actual_value)
        elif comparison_operator == "not empty":
            return self._assert_not_empty(actual_value)
        elif comparison_operator == "=":
            return self._assert_equal(actual_value, expected_value)
        elif comparison_operator == "≠":
            return self._assert_not_equal(actual_value, expected_value)
        elif comparison_operator == ">":
            return self._assert_greater_than(actual_value, expected_value)
        elif comparison_operator == "<":
            return self._assert_less_than(actual_value, expected_value)
        elif comparison_operator == "≥":
            return self._assert_greater_than_or_equal(actual_value, expected_value)
        elif comparison_operator == "≤":
            return self._assert_less_than_or_equal(actual_value, expected_value)
        elif comparison_operator == "null":
            return self._assert_null(actual_value)
        elif comparison_operator == "not null":
            return self._assert_not_null(actual_value)
        else:
            raise ValueError(f"Invalid comparison operator: {comparison_operator}")

    def process_conditions(self, variable_pool: VariablePool, conditions: Sequence[Condition]):
        input_conditions = []
        group_result = []

        for condition in conditions:
            actual_variable = variable_pool.get_any(condition.variable_selector)

            if condition.value is not None:
                variable_template_parser = VariableTemplateParser(template=condition.value)
                expected_value = variable_template_parser.extract_variable_selectors()
                variable_selectors = variable_template_parser.extract_variable_selectors()
                if variable_selectors:
                    for variable_selector in variable_selectors:
                        value = variable_pool.get_any(variable_selector.value_selector)
                        expected_value = variable_template_parser.format({variable_selector.variable: value})
                else:
                    expected_value = condition.value
            else:
                expected_value = None

            comparison_operator = condition.comparison_operator
            input_conditions.append(
                {
                    "actual_value": actual_variable,
                    "expected_value": expected_value,
                    "comparison_operator": comparison_operator
                }
            )

            result = self.evaluate_condition(actual_variable, expected_value, comparison_operator)
            group_result.append(result)

        return input_conditions, group_result

    def _assert_contains(self, actual_value: Optional[str | list], expected_value: str) -> bool:
        """
        Assert contains
        :param actual_value: actual value
        :param expected_value: expected value
        :return:
        """
        if not actual_value:
            return False

        if not isinstance(actual_value, str | list):
            raise ValueError('Invalid actual value type: string or array')

        if expected_value not in actual_value:
            return False
        return True

    def _assert_not_contains(self, actual_value: Optional[str | list], expected_value: str) -> bool:
        """
        Assert not contains
        :param actual_value: actual value
        :param expected_value: expected value
        :return:
        """
        if not actual_value:
            return True

        if not isinstance(actual_value, str | list):
            raise ValueError('Invalid actual value type: string or array')

        if expected_value in actual_value:
            return False
        return True

    def _assert_start_with(self, actual_value: Optional[str], expected_value: str) -> bool:
        """
        Assert start with
        :param actual_value: actual value
        :param expected_value: expected value
        :return:
        """
        if not actual_value:
            return False

        if not isinstance(actual_value, str):
            raise ValueError('Invalid actual value type: string')

        if not actual_value.startswith(expected_value):
            return False
        return True

    def _assert_end_with(self, actual_value: Optional[str], expected_value: str) -> bool:
        """
        Assert end with
        :param actual_value: actual value
        :param expected_value: expected value
        :return:
        """
        if not actual_value:
            return False

        if not isinstance(actual_value, str):
            raise ValueError('Invalid actual value type: string')

        if not actual_value.endswith(expected_value):
            return False
        return True

    def _assert_is(self, actual_value: Optional[str], expected_value: str) -> bool:
        """
        Assert is
        :param actual_value: actual value
        :param expected_value: expected value
        :return:
        """
        if actual_value is None:
            return False

        if not isinstance(actual_value, str):
            raise ValueError('Invalid actual value type: string')

        if actual_value != expected_value:
            return False
        return True

    def _assert_is_not(self, actual_value: Optional[str], expected_value: str) -> bool:
        """
        Assert is not
        :param actual_value: actual value
        :param expected_value: expected value
        :return:
        """
        if actual_value is None:
            return False

        if not isinstance(actual_value, str):
            raise ValueError('Invalid actual value type: string')

        if actual_value == expected_value:
            return False
        return True

    def _assert_empty(self, actual_value: Optional[str]) -> bool:
        """
        Assert empty
        :param actual_value: actual value
        :return:
        """
        if not actual_value:
            return True
        return False

    def _assert_not_empty(self, actual_value: Optional[str]) -> bool:
        """
        Assert not empty
        :param actual_value: actual value
        :return:
        """
        if actual_value:
            return True
        return False

    def _assert_equal(self, actual_value: Optional[int | float], expected_value: str) -> bool:
        """
        Assert equal
        :param actual_value: actual value
        :param expected_value: expected value
        :return:
        """
        if actual_value is None:
            return False

        if not isinstance(actual_value, int | float):
            raise ValueError('Invalid actual value type: number')

        if isinstance(actual_value, int):
            expected_value = int(expected_value)
        else:
            expected_value = float(expected_value)

        if actual_value != expected_value:
            return False
        return True

    def _assert_not_equal(self, actual_value: Optional[int | float], expected_value: str) -> bool:
        """
        Assert not equal
        :param actual_value: actual value
        :param expected_value: expected value
        :return:
        """
        if actual_value is None:
            return False

        if not isinstance(actual_value, int | float):
            raise ValueError('Invalid actual value type: number')

        if isinstance(actual_value, int):
            expected_value = int(expected_value)
        else:
            expected_value = float(expected_value)

        if actual_value == expected_value:
            return False
        return True

    def _assert_greater_than(self, actual_value: Optional[int | float], expected_value: str) -> bool:
        """
        Assert greater than
        :param actual_value: actual value
        :param expected_value: expected value
        :return:
        """
        if actual_value is None:
            return False

        if not isinstance(actual_value, int | float):
            raise ValueError('Invalid actual value type: number')

        if isinstance(actual_value, int):
            expected_value = int(expected_value)
        else:
            expected_value = float(expected_value)

        if actual_value <= expected_value:
            return False
        return True

    def _assert_less_than(self, actual_value: Optional[int | float], expected_value: str) -> bool:
        """
        Assert less than
        :param actual_value: actual value
        :param expected_value: expected value
        :return:
        """
        if actual_value is None:
            return False

        if not isinstance(actual_value, int | float):
            raise ValueError('Invalid actual value type: number')

        if isinstance(actual_value, int):
            expected_value = int(expected_value)
        else:
            expected_value = float(expected_value)

        if actual_value >= expected_value:
            return False
        return True

    def _assert_greater_than_or_equal(self, actual_value: Optional[int | float], expected_value: str) -> bool:
        """
        Assert greater than or equal
        :param actual_value: actual value
        :param expected_value: expected value
        :return:
        """
        if actual_value is None:
            return False

        if not isinstance(actual_value, int | float):
            raise ValueError('Invalid actual value type: number')

        if isinstance(actual_value, int):
            expected_value = int(expected_value)
        else:
            expected_value = float(expected_value)

        if actual_value < expected_value:
            return False
        return True

    def _assert_less_than_or_equal(self, actual_value: Optional[int | float], expected_value: str) -> bool:
        """
        Assert less than or equal
        :param actual_value: actual value
        :param expected_value: expected value
        :return:
        """
        if actual_value is None:
            return False

        if not isinstance(actual_value, int | float):
            raise ValueError('Invalid actual value type: number')

        if isinstance(actual_value, int):
            expected_value = int(expected_value)
        else:
            expected_value = float(expected_value)

        if actual_value > expected_value:
            return False
        return True

    def _assert_null(self, actual_value: Optional[int | float]) -> bool:
        """
        Assert null
        :param actual_value: actual value
        :return:
        """
        if actual_value is None:
            return True
        return False

    def _assert_not_null(self, actual_value: Optional[int | float]) -> bool:
        """
        Assert not null
        :param actual_value: actual value
        :return:
        """
        if actual_value is not None:
            return True
        return False

    @classmethod
    def _extract_variable_selector_to_variable_mapping(cls, node_data: BaseNodeData) -> dict[str, list[str]]:
        """
        Extract variable selector to variable mapping
        :param node_data: node data
        :return:
        """
        return {}
