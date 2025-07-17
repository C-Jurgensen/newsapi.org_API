__constraintAttributes = {}

class ConstraintFail(Exception):
    def __init__(self):...

def check_constraints(key):
    return __constraintAttributes.get(key)

def register_constraint_handler(name):
    def register_func(func):
        if __constraintAttributes.get(name) is not None:
            raise KeyError('Constraint %s is already registered.' % name)
        __constraintAttributes[name] = func
    return register_func

@register_constraint_handler("length")
class LengthLimit:

    def __init__(self, len_limit:int):
        self.__check_type(len_limit)
        self.limit:int = len_limit

    @staticmethod
    def __check_type(length:int):
        if type(length) != int:
            raise TypeError("length must be of type int but got: %s" % type(length))

    def __call__(self, value:any):
        if len(value) > self.limit:
            raise ConstraintFail


@register_constraint_handler("type")
class TypeCheck:

    def __init__(self, obj_type:type):
        self.objType = obj_type

    def __call__(self, obj:any):
        if type(obj) != self.objType:
            raise ConstraintFail