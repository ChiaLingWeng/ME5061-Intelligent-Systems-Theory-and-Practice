from typing import Any
from .fuzzy_set import FuzzySet
from .fuzzy_variable import FuzzyVariable


class FuzzyClause:
    """
    A fuzzy clause of the type 'variable is fset' used in fuzzy IF ... THEN ... rules
    clauses can be antecedent (IF part) or consequent (THEN part)
    """
    def __init__(self, var: Any, f_set: Any) -> None:
        """
        Initializes the fuzzy clause
        :param var: the clause variable in 'variable is fset'
        :param f_set: the clause set in 'variable is fset'
        """
        if f_set is None:
            raise Exception('f_set is NoneType!')
        if f_set.name == '':
            raise Exception(str(f_set), 'No set\'s name!')
        self.var = var
        self.f_set = f_set

    def __str__(self) -> str:
        """
        String representation of the clause.
        :return: string representation of the clause in the form A is x
        """
        return f'{self.var.name} is {self.f_set.name}'

    @property
    def variable_name(self) -> str:
        """
        Returns the name of the clause variable
        :return: name of  the variable
        """
        return self.var.name

    @property
    def fset_name(self) -> str:
        """
        Returns the name of the clause
        :return: name of set
        """
        return self.f_set.name

    def evaluate_antecedent(self) -> float:
        """
        Used when set is antecedent, it returns the set degree of membership.
        :return: the set degree of membership given a value for that variable.
                    This value is determined at an earlier stage and stored in the set
        """
        return self.f_set.last_dom_value

    def evaluate_consequent(self, dom: Any) -> None:
        """
        Used when clause is consequent.
        :param dom: degree of membership, or scalar value from the antecedent clauses
        :return: Fuzzy Set Type1, a set resulting from min operation with the scalar value
        """
        self.var.add_rule_contribution(self.f_set.min_scalar(dom))

