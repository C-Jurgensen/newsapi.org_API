from NewsApi.BaseClasses.Params import Param

__all__=["Params"]


class Params:
    country = Param("country", type=str, length=2)
    sources = Param("sources", type=str, length=2)
    category = Param("category", type=str)
    query = Param("q")
    size = Param("pageSize", type=int)
    page = Param("page", type=int)
    apiKey=Param("apiKey", type=str)
    sortBy=Param("sortBy", options=["relevancy", "popularity", "publishedAt"], type=list)
    searchIn=Param("search_in", options=["title", "description", "content"], type=list)
    excludeDomains=Param("excludeDomains", type=list)
    domains=Param("domains", type=list)
    dateFrom=Param("from")
    dateTo=Param("to")
    lang=Param("language", type=str, length=2)

    @classmethod
    def __class_getitem__(cls, item):
        attribute = cls.__dict__[item]
        if not isinstance(attribute, Param):
            raise TypeError('%s for key %s is not a declared parameter and should not be returned.' % (attribute, item))
        return attribute
