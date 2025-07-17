from NewsApi.HeaderGroupConsts import HeaderGroups
from URLs import URL
from ApiKey import ApiKey

from enum import Enum

__all__ = ["APIHandler"]

class UrlConstants(Enum):
    Retrieve_Top_Stories=...


class APIHandler:
    """
    If you need to run saved urls please use and instance of this class else run manually passing the url into the
    response handler.
    """

    def __init__(self, api_key:str):
        self.__apiKey = ApiKey(api_key)

    def __getitem__(self, url_name:str) -> URL | None:
        try:
            instance_attribute = self.__getattribute__(url_name)
            return instance_attribute if isinstance(instance_attribute, URL) else None
        except AttributeError:
            pass

    def __setitem__(self, name, url:URL):
        self.add_url(name, url)

    @property
    def api_key(self):
        return str(self.__apiKey)

    @api_key.setter
    def api_key(self, key):
        if not isinstance(key, str):
            raise TypeError('apiKey needs to be of type string.')
        self.__apiKey.key = key

    def add_url(self, url_name:str, url_obj:URL, overwrite:bool=True):
        """
        Adds a named url to the handler. These will be added to the attributes of the handler.
        :param url_name: The name to be added in attributes to access the url.
        :param url_obj: The URL object to be assigned to the attribute.
        :param overwrite: Whether the current attribute if exists should be overwritten or not.
        """
        if takenCheck := self.__getattribute__(url_name):
            if not overwrite:
                raise KeyError('"%s" is already defined.' % url_name)
            if not isinstance(takenCheck, URL):
                raise KeyError("Key %s is assigned to an object other than type 'URL'" % url_name)
        url_obj.set_api_key(self.__apiKey)
        self.__setattr__(url_name, url_obj)
