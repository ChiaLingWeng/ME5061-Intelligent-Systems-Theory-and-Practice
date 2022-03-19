from .fuzzy_variable import FuzzyVariable


class FuzzyVariableInput(FuzzyVariable):

    def __init__(self, name: str, min_val: float, max_val: float, res: float) -> None:
        super().__init__(name, min_val, max_val, res)

    def fuzzify(self, value: float) -> None:
        """
        Performs fuzzification of the variable. used when the variable is an input one
        """
        # get dom for each set and store it - it will be required for each rule
        for set_name, f_set in self.sets.items():
            f_set.last_dom_value = f_set[value]

    def fuzzify_info(self, value: float) -> str:
        """
        Performs fuzzification of the variable. used when the
        variable is an input one
        :param value: input value for the variable
        """
        # get dom for each set and store it - it will be required for each rule
        for set_name, f_set in self.sets.items():
            f_set.last_dom_value = f_set[value]
        res = [self._name, '\n']
        for _, f_set in self.sets.items():
            res.append(f_set.name)
            res.append(str(f_set.last_dom_value))
            res.append('\n')
        return ' '.join(res)
