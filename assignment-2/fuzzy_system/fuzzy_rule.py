from typing import Any
from .fuzzy_clause import FuzzyClause


class FuzzyRule:
    """
    A fuzzy rule of type
    IF [antecedent clauses] THEN [consequent clauses]
    """

    def __init__(self) -> None:
        """
        Initializes the fuzzy rule
        Two data structures are necessary:
        1. Antecedent clauses list
        2. Consequent clauses list
        """
        self.antecedents = []
        self.consequents = []

    def __str__(self) -> str:
        """
        String representation of the rule
        :return: string representation of the rule in the form IF [antecedent clauses] THEN [consequent clauses]
        """
        ante = ' and '.join(map(str, self.antecedents))
        cons = ' and '.join(map(str, self.consequents))
        return f'IF {ante} THEN {cons}'

    def add_antecedent_clause(self, var: Any, f_set: Any) -> None:
        """
        TODO:
         Creat new antecedent clause with variable `var` and fuzzy set `f_set` using FuzzyClause.
         Adds an antecedent clause to the antecedent list.
        :param var: the clause variable in 'variable is set'
        :param f_set: another fuzzy set
        """
        # Write your code below

        new_antecedent_clause = FuzzyClause(var,f_set)
        self.antecedents.append(new_antecedent_clause)

    def add_consequent_clause(self, var: Any, f_set: Any) -> None:
        """
        TODO:
         Creat new consequent clause with variable `var` and fuzzy set `f_set` using FuzzyClause.
         Adds an consequent clause to the consequent list.
        Adds a consequent clause to the rule
        :param var: the clause variable in 'variable is set'
        :param f_set: another fuzzy set
        """
        # Write your code below
        new_consequent_clause = FuzzyClause(var,f_set)
        self.consequents.append(new_consequent_clause)

    def evaluate(self) -> None:
        """
        Evaluation of the rule.
        The antecedent clauses are executed and the minimum degree of membership is retained.
        This is used in the consequent clauses to min with the consequent set
        The values are returned in a dict of the form {variable_name: scalar min set, ...}
        :return: a dict resulting sets in the form {variable_name: scalar min set, ...}
        """
        # rule dom initialize to 1 as min operator will be performed
        rule_strength = 1
        # execute all antecedent clauses, keeping the minimum of the
        # returned doms to determine the rule strength
        for ante_clause in self.antecedents:
            rule_strength = min(ante_clause.evaluate_antecedent(), rule_strength)
        # execute consequent clauses, each output variable will update its output_distribution set
        for consequent_clause in self.consequents:
            consequent_clause.evaluate_consequent(rule_strength)

    def evaluate_info(self) -> str:
        """
        Evaluation of the rule.
        The antecedent clauses are executed and the minimum degree of membership is retained.
        This is used in teh consequent clauses to min with the consequent set
        The values are returned in a dict of the form {variable_name: scalar min set, ...}
        :return:  a dict that resulting sets in the form {variable_name: scalar min set, ...}
        """
        # rule dom initialize to 1 as min operator will be performed
        rule_strength = 1
        # execute all antecedent clauses, keeping the minimum of the
        # returned doms to determine the rule strength
        for ante_clause in self.antecedents:
            rule_strength = min(ante_clause.evaluate_antecedent(), rule_strength)
        # execute consequent clauses, each output variable will update its output_distribution set
        for consequent_clause in self.consequents:
            consequent_clause.evaluate_consequent(rule_strength)
        return f'{rule_strength} : {self}'
