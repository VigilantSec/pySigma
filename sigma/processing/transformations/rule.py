from abc import abstractmethod
from typing import (
    Any,
    List,
    Dict,
    Optional,
    Union,
)
from dataclasses import dataclass, field
import sigma
from sigma.correlations import SigmaCorrelationRule
from sigma.processing.transformations.base import (
    Transformation,
)
from sigma.rule import SigmaLogSource, SigmaRule
from sigma.rule.attributes import SigmaRuleTag


@dataclass
class ChangeLogsourceTransformation(Transformation):
    """Replace log source as defined in transformation parameters."""

    category: Optional[str] = field(default=None)
    product: Optional[str] = field(default=None)
    service: Optional[str] = field(default=None)

    def apply(self, rule: SigmaRule) -> None:
        super().apply(rule)
        logsource = SigmaLogSource(self.category, self.product, self.service)
        rule.logsource = logsource


@dataclass
class SetCustomAttributeTransformation(Transformation):
    """
    Sets an arbitrary custom attribute on a rule, that can be used by a backend during processing.
    """

    attribute: str
    value: Any

    def apply(self, rule: Union[SigmaRule, SigmaCorrelationRule]) -> None:
        super().apply(rule)
        rule.custom_attributes[self.attribute] = self.value


@dataclass
class AddTagTransformation(Transformation):
    """
    Add one or multiple tags to the Sigma rule.
    """

    tag: Union[str, List[str]]

    def apply(
        self, rule: SigmaRule
    ) -> None:
        super().apply(rule)
        if isinstance(self.tag, str):
            rule.tags.append(SigmaRuleTag.from_str(self.tag))
        elif isinstance(self.tag, list):
            rule.tags.extend([SigmaRuleTag.from_str(tag) for tag in self.tag])
        rule.tags = list(set(rule.tags))
