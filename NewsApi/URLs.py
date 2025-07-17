from NewsApi.HeaderGroups import HeaderGroup
from HeaderGroupConsts import HeaderGroups

__all__=["URL"]


class URL:

    __baseURL = 'https://newsapi.org/v2/'

    def __init__(self, header: HeaderGroup = HeaderGroups.top.value, set_params:tuple | bool = False, **param_defaults):
        """
        Declares a url object for parameters to be entered into.
        :param header: The headerGroup to use.
        :param editable_params: A keyword dictionary of parameters to be searched.
        """
        self.__header = header
        self.__setParams:set|bool = set(set_params) if type(set_params) == tuple else set_params
        self.__paramDefaults:dict|None = param_defaults

    @property
    def param_defaults(self):
        return self.__paramDefaults.copy()

    def update_defaults(self, **params):
        """
        Changes the default parameter values.
        """
        self.__header.check_params(**params) #Check if the new values are acceptable for the header and param constraints.
        self.__paramDefaults.update(params)

    def form_url(self, **params):
        self.__header.check_params(**params)
        url_structure = []
        if self.__header is not None:
            url_structure.append('%s'%self.__header.name)
        if type(self.__setParams) == set and len(self.__setParams.intersection(set(params.keys()))) != 0:
            # Checks for any parameters that were set as non-editable.
            raise KeyError('The following parameters were set as non-editable: %s' \
                           % self.__setParams.intersection(set(params.keys())))
        for param in set(self.__paramDefaults.keys()).difference(set(params.keys())):
            # Updates the parameters with default params that weren't overwritten.
            params[param] = self.__paramDefaults[param]
        return self.__baseURL+'/'.join(url_structure)+'?'+'&'.join(['%s=%s' % (param, value) for param, value in params.items()])

    def __str__(self):
        return self.form_url()

    def __call__(self):
        return self.form_url()
