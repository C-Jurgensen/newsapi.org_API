from .Params import Param

__all__=["HeaderGroup"]

class HeaderGroup:

    def __init__(self, name:str, *params:Param):

        self.__name:str = name
        self.__params:dict[str,Param] = {} #A dictionary of the param name and parameter.
        self.add_params(*params) #Adding initial passed in parameters.

    @property
    def name(self):
        """
        Returns the name of the header group.
        """
        return self.__name

    def add_params(self, *params:Param):
        """
        Adds in the new parameter value sto the params dictionary.
        :param params: An iterable of initialized parameters to be assigned to the header group.
        """
        for param in params:
            if isinstance(param, Param):
                raise TypeError('Param needs to be of type param. Got: %s' % type(param))
            self.__params[param.name] = param

    def check_params(self, **params):
        """
        Checks if the passed in parameters are valid for the header.
        :param params: A keyword value pair of params passed in to be checked.
        """
        for param, value in params.items():
            self.__params[param].validate_param(value)

    def __str__(self):
        return self.__name

    def __repr__(self):
        return self.__name