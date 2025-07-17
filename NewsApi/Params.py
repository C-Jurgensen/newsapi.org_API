from NewsApi.Constraints import ParamConstraint

from typing import Literal, Union, override

__all__ = ["Param"]

class _ParamChecker:

    def __init__(self, options:set[Literal]):
        #print(options)
        self.options = options

    def __call__(self, param_val):
        if not isinstance(param_val, (int, str)):
            raise TypeError('You must use a custom check for checking literals other than integers and strings.')
        if param_val not in self.options:
            raise ValueError('Value %s was not found in the declared options available.' % param_val)


class Param(ParamConstraint):

    def __init__(self, name: str, *options: Union[str,int,any], checker = None, **kwargs):
        self.name = name
        if len(options) != 0:
            if not isinstance(options, set):
                #print(isinstance(options, set))
                #print(options)
                hashed_options = set()
                for option in options:
                    hashed_options.add(option)
            else:
                hashed_options:set = options
            self.checker = _ParamChecker(hashed_options) if checker is None else checker
        else:
            self.checker = checker
        super().__init__(**kwargs)

    def __call__(self, value):
        if self.checker is not None:
            self.checker(value)
        super().check_constraints(value)
