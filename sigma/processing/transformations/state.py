from typing import Any
from dataclasses import dataclass
import sigma
from sigma.processing.transformations.base import Transformation
from sigma.rule import SigmaRule


@dataclass
class SetStateTransformation(Transformation):
    """Set pipeline state key to value."""

    key: str
    val: Any

    def apply(self, rule: SigmaRule) -> None:
        super().apply(rule)
        self._pipeline.state[self.key] = self.val


@dataclass
class AddStateTransformation(Transformation):
    """Add a value or values to a pipeline state key."""

    key: str
    val: Any

    def apply(self, rule: SigmaRule) -> None:
        super().apply(rule)
        if self.key not in self._pipeline.state:
            self._pipeline.state[self.key] = self.val if isinstance(self.val, list) else [self.val]
        else:
            if not isinstance(self._pipeline.state[self.key], list):
                self._pipeline.state[self.key] = [self._pipeline.state[self.key]]
            if isinstance(self.val, list):
                self._pipeline.state[self.key].extend(self.val)
            else:
                self._pipeline.state[self.key].append(self.val)
        self._pipeline.state[self.key] = list(set(self._pipeline.state[self.key]))
