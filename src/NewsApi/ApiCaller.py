__all__ = ['call_api']

from requests import request

from dataclasses import dataclass


@dataclass
class Source:
    id:str
    name:str


@dataclass
class Author:
    firstName:str
    lastName:str = None


@dataclass
class Article:
    source:Source
    author:Author
    title:str
    description:str
    url:str
    urlToImage:str
    content:str
    publishedAt:str


@dataclass
class MetaData:
    totalResults:int
    status:str


class Authors:

    def __init__(self):
        self.authors = {}

    def add_author(self, author_name:str | None) -> Author | None:
        if author_name is None:
            return
        authorCheck = self[author_name]
        if authorCheck:
            return authorCheck
        if author_name:
            self.authors[author_name] = Author(*author_name.split(" ", 1))

    def __getitem__(self, name:str):
        return self.authors.get(name)


class Sources:

    def __init__(self):
        self.sources_id = dict()
        self.sources_name = dict()

    def __make_source(self, ID, name):
        newSource = Source(ID, name)
        if ID:
            self.sources_id[ID] = newSource
        self.sources_name[name] = newSource

    def add_source(self, source_info:dict, *, override_source=False, return_if_found=False):
        ID = source_info.get('id')
        name = source_info.get('name')
        match override_source:
            case False:
                if ID is None:
                    sourceObj = self.lookup_source_name(name)
                else:
                    sourceObj = self.lookup_source_id(ID)
                if sourceObj:
                    if not return_if_found:
                        return None
                    else:
                        return sourceObj
                else:
                    self.__make_source(ID, name)
            case True:
                self.__make_source(ID, name)


    def lookup_source_name(self, source_name:str):
        return self.sources_id.get(source_name)

    def lookup_source_id(self, source_id:int):
        return self.sources_name.get(source_id)


class Articles(Authors, Sources):

    def __init__(self, articles:list):
        Authors.__init__(self)
        Sources.__init__(self)
        self.articles:list[Article] = list()
        for article in articles:
            print(article)
            article['source'] = Sources.add_source(self, article.get('source'), return_if_found=True)
            article['author'] = Authors.add_author(self, article.get('author'))
            self.articles.append(Article(**article))


class ApiResponse(Articles):

    def __init__(self, response:dict):
        self.metadata:MetaData = MetaData\
            (
                response.get('status'),
                response.get('totalResults')
            )
        super().__init__(response.get('articles', list()))


def call_api(url:str) -> ApiResponse:
    return ApiResponse(request('GET', url).json())
