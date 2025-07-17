from enum import Enum

from BaseClasses.HeaderGroups import HeaderGroup
from ParamConstraintsConsts import Params as p


class HeaderGroups(Enum):
    top=HeaderGroup("top-headlines", p.apiKey, p.country, p.category, p.sources, p.query, p.size, p.page, p.lang)
    everything=HeaderGroup("everything", p.apiKey, p.query, p.searchIn, p.sources, p.domains, p.domains, p.excludeDomains,
                           p.dateFrom, p.dateTo, p.sortBy, p.size, p.page, p.lang)
