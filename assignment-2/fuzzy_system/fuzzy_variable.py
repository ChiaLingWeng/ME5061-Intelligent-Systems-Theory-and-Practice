from typing import Any
from .fuzzy_set import FuzzySet
import matplotlib as plt

class FuzzyVariable:
    """
    A type-1 fuzzy variable that is mage up of a number of type-1 fuzzy sets
    """

    def __init__(self, name: str, min_val: float, max_val: float, res: float) -> None:
        """
        Creates a new type-1 fuzzy variable (universe)
        :param name: the name of variable
        :param min_val: minimum value of variable
        :param max_val: maximum value of variable
        :param res: resolution of variable
        """
        self.sets = {}
        self.max_val = max_val
        self.min_val = min_val
        self.res = res
        self.name = name

    def __str__(self) -> None:
        return ', '.join(self.sets.keys())

    def add_set(self, name: str, f_set: Any) -> None:
        """
        TODO:
         Adds a fuzzy set into sets dictionary of the variable
        :param name: name of the set
        :param f_set: the fuzzy set
        """
        # write code below
        self.sets[name] = f_set

    def get_set(self, name: str) -> Any:
        """
        TODO:
         Return a fuzzy set given the name
        :param name: set name
        """
        # Write your code below
        return self.sets[name]

    def add_triangular(self, name: str, low: float, mid: float, high: float) -> Any:
        """
        TODO:
         Add triangular membership function to the variable
        :param name: set name
        :param low: a value
        :param mid: m value
        :param high: b value
        """
        new_set = None
        # write the code below
        # use create triangular function

        new_set = FuzzySet.create_triangular(name=name,domain_min=self.min_val,domain_max=self.max_val,res=self.res,a=low,m=mid,b=high )
        self.add_set(name,new_set)
        return new_set

    def add_trapezoidal(self, name: str, a: float, b: float, c: float, d: float) -> Any:
        """
        TODO:
         Add trapezoidal membership function to the variable
        :param name: set name
        :param a: a value
        :param b: b value
        :param c: c value
        :param d: d value
        """
        new_set = None
        # Write your code below

        new_set = FuzzySet.create_trapezoidal(name,domain_min=self.min_val,domain_max=self.max_val,res=self.res,a=a,b=b,c=c,d=d )
        self.add_set(name,new_set)


        return new_set

    def plot_variable(self, ax: Any = None, show: bool = True) -> None:
        """
        Plots a graphical representation of the fuzzy variable
        Reference:
        ----------
            https://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot
        """
        if ax is None:
            ax = plt.subplot(111)
        for n, s in self.sets.items():
            ax.plot(s.get_domain_elements(), s.get_dom_elements(), label=n)
        # Shrink current axis by 20%
        pos = ax.get_position()
        ax.set_position([pos.x0, pos.y0, pos.width * 0.8, pos.height])
        ax.grid(True, which='both', alpha=0.4)
        ax.set_title(self.name)
        ax.set(xlabel='x', ylabel='$\mu (x)$')
        # Put a legend to the right of the current axis
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        if show:
            plt.show()
