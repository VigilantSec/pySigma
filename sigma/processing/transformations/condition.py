from abc import abstractmethod
from sigma.conditions import SigmaCondition
from typing import (
    Any,
    List,
    Dict,
    Optional,
    Union,
)
from dataclasses import dataclass, field
import random
import string
import sigma
from sigma.processing.transformations.base import (
    ConditionTransformation,
)
from sigma.rule import SigmaRule, SigmaDetection


@dataclass
class AddConditionTransformation(ConditionTransformation):
    """
    Add a condition expression to rule conditions.

    If template is set to True the condition values are interpreted as string templates and the
    following placeholders are replaced:

    * $category, $product and $service: with the corresponding values of the Sigma rule log source.
    """

    conditions: Dict[str, Union[str, List[str]]] = field(default_factory=dict)
    name: Optional[str] = field(default=None, compare=False)
    template: bool = False
    negated: bool = False
    prepend: bool = False

    def __post_init__(self):
        if self.name is None:  # generate random detection item name if none is given
            self.name = "_cond_" + ("".join(random.choices(string.ascii_lowercase, k=10)))

    def apply(self, rule: SigmaRule) -> None:
        if isinstance(rule, SigmaRule):
            if self.template:
                conditions = {
                    field: (
                        [
                            string.Template(item).safe_substitute(
                                category=rule.logsource.category,
                                product=rule.logsource.product,
                                service=rule.logsource.service,
                            )
                            for item in value
                        ]
                        if isinstance(value, list)
                        else string.Template(value).safe_substitute(
                            category=rule.logsource.category,
                            product=rule.logsource.product,
                            service=rule.logsource.service,
                        )
                    )
                    for field, value in self.conditions.items()
                }
            else:
                conditions = self.conditions

            rule.detection.detections[self.name] = SigmaDetection.from_definition(conditions)
            self.processing_item_applied(rule.detection.detections[self.name])
            super().apply(rule)

    def apply_condition(self, cond: SigmaCondition) -> None:
        negate_or_not = "not " if self.negated else ""
        if self.prepend:
            cond.condition = f"{negate_or_not}{self.name} and ({cond.condition})"
        else:
            cond.condition = f"({cond.condition}) and {negate_or_not}{self.name}"
