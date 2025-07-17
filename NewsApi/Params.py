from NewsApi.Constraints import ParamConstraint

from typing import Literal, Union, override

__all__ = ["Param"]

class _ParamChecker:

    def __init__(self, options:set[Literal]):
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
            options = set(options)
            self.checker = _ParamChecker(options) if checker is not None else checker
        super().__init__(**kwargs)

    def __call__(self, value):
        super().check_constraints(value)
