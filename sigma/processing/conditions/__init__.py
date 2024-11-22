from sigma.processing.conditions.base import (
    ProcessingCondition,
    DetectionItemProcessingCondition,
    FieldNameProcessingCondition,
    RuleProcessingCondition,
)
from typing import Dict

from sigma.processing.conditions.fields import ExcludeFieldCondition, IncludeFieldCondition
from sigma.processing.conditions.rule import (
    IsSigmaCorrelationRuleCondition,
    IsSigmaRuleCondition,
    LogsourceCondition,
    RuleAttributeCondition,
    RuleContainsDetectionItemCondition,
    RuleContainsDetectionItemField,
    RuleContainsDetectionItemFieldRegex,
    RuleContainsKeywordDetectionItem,
    DetectionItemIsField,
    DetectionItemIsFieldRegex,
    DetectionItemIsKeyword,
    RuleContainsFieldCondition,
    RuleTagCondition,
)
from sigma.processing.conditions.state import (
    DetectionItemProcessingItemAppliedCondition,
    DetectionItemProcessingStateCondition,
    FieldNameProcessingItemAppliedCondition,
    FieldNameProcessingStateCondition,
    RuleProcessingItemAppliedCondition,
    RuleProcessingStateCondition,
)
from sigma.processing.conditions.values import (
    ContainsWildcardCondition,
    IsNullCondition,
    MatchStringCondition,
)


rule_conditions: Dict[str, RuleProcessingCondition] = {
    "logsource": LogsourceCondition,
    "contains_detection_item": RuleContainsDetectionItemCondition,
    "contains_detection_item_field": RuleContainsDetectionItemField,
    "contains_detection_item_field_regex": RuleContainsDetectionItemFieldRegex,
    "contains_keyword_detection_item": RuleContainsKeywordDetectionItem,
    "contains_field": RuleContainsFieldCondition,
    "processing_item_applied": RuleProcessingItemAppliedCondition,
    "processing_state": RuleProcessingStateCondition,
    "is_sigma_rule": IsSigmaRuleCondition,
    "is_sigma_correlation_rule": IsSigmaCorrelationRuleCondition,
    "rule_attribute": RuleAttributeCondition,
    "tag": RuleTagCondition,
}
detection_item_conditions: Dict[str, DetectionItemProcessingCondition] = {
    "match_string": MatchStringCondition,
    "contains_wildcard": ContainsWildcardCondition,
    "is_null": IsNullCondition,
    "is_field": DetectionItemIsField,
    "is_field_regex": DetectionItemIsFieldRegex,
    "is_keyword": DetectionItemIsKeyword,
    "processing_item_applied": DetectionItemProcessingItemAppliedCondition,
    "processing_state": DetectionItemProcessingStateCondition,
}
field_name_conditions: Dict[str, DetectionItemProcessingCondition] = {
    "include_fields": IncludeFieldCondition,
    "exclude_fields": ExcludeFieldCondition,
    "processing_item_applied": FieldNameProcessingItemAppliedCondition,
    "processing_state": FieldNameProcessingStateCondition,
}
