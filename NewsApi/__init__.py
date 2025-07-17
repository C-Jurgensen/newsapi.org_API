from NewsApi.HeaderGroupConsts import HeaderGroups
from URLs import URL

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
        self.apiKey = api_key

    def __getitem__(self, url_name:str) -> URL | None:
        try:
            instance_attribute = self.__getattribute__(url_name)
            return instance_attribute if isinstance(instance_attribute, URL) else None
        except AttributeError:
            pass

    def __setitem__(self, name, url:URL):
        self.add_url(name, url)

    def add_url(self, url_name:str, url_obj:URL, overwrite:bool=True):
        if takenCheck := self[url_name]:
            if not overwrite:
                raise KeyError('"%s" is already defined.' % url_name)
            if takenCheck is None:
                raise KeyError("Key %s is assigned to an object other than type 'URL'" % url_name)
        self.__setattr__(url_name, url_obj)

#Testing
if __name__ == "__main__":
    handler = APIHandler("Test")
    handler.add_url("Test",URL(HeaderGroups["top"].value))
    print(handler.Test)
    urlTest = URL(HeaderGroups["top"].value)
    print(urlTest.form_url(language="en"))
