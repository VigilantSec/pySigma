from typing import Dict
from sigma.processing.transformations.base import Transformation
from sigma.processing.transformations.condition import AddConditionTransformation
from sigma.processing.transformations.detection_item import DropDetectionItemTransformation
from sigma.processing.transformations.failure import (
    DetectionItemFailureTransformation,
    RuleFailureTransformation,
)
from sigma.processing.transformations.fields import (
    AddFieldTransformation,
    AddFieldnamePrefixTransformation,
    AddFieldnameSuffixTransformation,
    FieldFunctionTransformation,
    FieldMappingTransformation,
    FieldPrefixMappingTransformation,
    RemoveFieldTransformation,
    SetFieldTransformation,
)
from sigma.processing.transformations.meta import NestedProcessingTransformation
from sigma.processing.transformations.placeholder import (
    QueryExpressionPlaceholderTransformation,
    ValueListPlaceholderTransformation,
    WildcardPlaceholderTransformation,
)
from sigma.processing.transformations.rule import (
    ChangeLogsourceTransformation,
    SetCustomAttributeTransformation,
    AddTagTransformation,
)
from sigma.processing.transformations.state import (
    SetStateTransformation,
    AddStateTransformation,
)
from sigma.processing.transformations.values import (
    ConvertTypeTransformation,
    HashesFieldsDetectionItemTransformation,
    MapStringTransformation,
    RegexTransformation,
    ReplaceStringTransformation,
    ReplaceRegexTransformation,
    SetValueTransformation,
    CaseTransformation,
)

transformations: Dict[str, Transformation] = {
    "field_name_mapping": FieldMappingTransformation,
    "field_name_prefix_mapping": FieldPrefixMappingTransformation,
    "field_name_transform": FieldFunctionTransformation,
    "drop_detection_item": DropDetectionItemTransformation,
    "hashes_fields": HashesFieldsDetectionItemTransformation,
    "field_name_suffix": AddFieldnameSuffixTransformation,
    "field_name_prefix": AddFieldnamePrefixTransformation,
    "wildcard_placeholders": WildcardPlaceholderTransformation,
    "value_placeholders": ValueListPlaceholderTransformation,
    "query_expression_placeholders": QueryExpressionPlaceholderTransformation,
    "add_condition": AddConditionTransformation,
    "change_logsource": ChangeLogsourceTransformation,
    "add_field": AddFieldTransformation,
    "add_tag": AddTagTransformation,
    "remove_field": RemoveFieldTransformation,
    "set_field": SetFieldTransformation,
    "replace_string": ReplaceStringTransformation,
    "replace_regex": ReplaceRegexTransformation,
    "map_string": MapStringTransformation,
    "set_state": SetStateTransformation,
    "add_state": AddStateTransformation,
    "regex": RegexTransformation,
    "set_value": SetValueTransformation,
    "convert_type": ConvertTypeTransformation,
    "rule_failure": RuleFailureTransformation,
    "detection_item_failure": DetectionItemFailureTransformation,
    "set_custom_attribute": SetCustomAttributeTransformation,
    "nest": NestedProcessingTransformation,
    "case": CaseTransformation,
}
