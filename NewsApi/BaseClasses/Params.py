from .Constraints import ParamConstraint

__all__ = ["Param"]

class Param(ParamConstraint):

    def __init__(self, name: str, /, options:list=None, **kwargs):
        self.name = name
        super().__init__(**kwargs)

    def validate_param(self, value):
        self(value)