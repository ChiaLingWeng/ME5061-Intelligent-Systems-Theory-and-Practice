from typing import Any, Tuple
from .fuzzy_variable import FuzzyVariable
from .fuzzy_set import FuzzySet


class FuzzyVariableOutput(FuzzyVariable):
    def __init__(self, name: str, min_val: float, max_val: float, res: float) -> None:
        super().__init__(name, min_val, max_val, res)
        self.output_distribution = FuzzySet(name, min_val, max_val, res)


    def clear_output_distribution(self) -> None:
        self.output_distribution.clear_set()

    def add_rule_contribution(self, rule_consequence: Any) -> None:
        self.output_distribution = self.output_distribution.union(rule_consequence)

    def get_crisp_output(self) -> Any:
        #self.output_distribution is a FuzzySet
        return self.output_distribution.defuzzify_cog()

    def get_crisp_output_info(self) -> Tuple[Any, Any]:
        return self.output_distribution.defuzzify_cog(), self.output_distribution
