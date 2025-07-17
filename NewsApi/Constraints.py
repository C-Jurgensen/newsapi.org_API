from NewsApi.RegisteredConstraints import check_constraints

__all__=["ParamConstraint"]


class ParamConstraint:

    def __init__(self, **kwargs):
        self.__constraints = []
        for key, value in kwargs.items():
            constraint_handler = check_constraints(key)
            if constraint_handler is None:
                raise KeyError('No handler found for constraint %s' % key)
            self.__constraints.append(constraint_handler(value))

    def check_constraints(self, value:any):
        for constraint in self.__constraints:
            constraint(value)
