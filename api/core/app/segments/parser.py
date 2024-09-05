import re

from core.workflow.entities.variable_pool import VariablePool

from . import SegmentGroup, factory

VARIABLE_PATTERN = re.compile(r'\{\{#([a-zA-Z0-9_]{1,50}(?:\.[a-zA-Z_][a-zA-Z0-9_]{0,29}){1,10})#\}\}')


def convert_template(*, template: str, variable_pool: VariablePool):
    parts = re.split(VARIABLE_PATTERN, template)
    segments = []
    for part in filter(lambda x: x, parts):
        if '.' in part and (value := variable_pool.get(part.split('.'))):
            segments.append(value)
        else:
            segments.append(factory.build_segment(part))
    return SegmentGroup(value=segments)
