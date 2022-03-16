from enum import Enum
import abc
from shorty.errors import APIError
from marshmallow import Schema, fields, INCLUDE,ValidationError




# This class(Enum) includes supported link shorter providers
class ShorthenLinkType(Enum):
  TINYURL = "TINYURL"
  BITLY = "BITLY"

# This function checks wheter given provider in the ShorthenLinkType enum
def providerValidate(data):
    acceptedProviderList =[e.value for e in ShorthenLinkType]
    if data not in acceptedProviderList:
        acceptedProviderListString = ",".join(acceptedProviderList)
        raise ValidationError("provider must be one of: "+acceptedProviderListString)

# This class provides necessary variables with control of their validation
class ShorthenLinkSchema(Schema):
    class Meta:
        unknown = INCLUDE
    url = fields.Str(required=True,error_messages={"required":  "url is required"},)
    provider = fields.Str(validate=providerValidate)
    
# This class provides utility functions for shorthen an url by strategy pattern
# 1. use_provider(self,url): returns the short version of the url by given strategy by the class
# 2. use_providers(self,url,others): returns the short version of the url by strategy of current class and in case of fallback other classes' strategy
class LinkShorter:
    def __init__(self, strategy):
        self._strategy = strategy

    def use_provider(self,url):
        return self._strategy.short_link(url)

    def use_providers(self,url,others):
        try:
            return self._strategy.short_link(url)
        except:
            for provider in others:
                try:
                    return provider._strategy.short_link(url)
                except:
                    continue
            raise APIError(503,"All providers are unavailable")
    


class LinkShorterStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def short_link(self):
        pass

