from shorty.model.link_shorter_model import ShorthenLinkType,LinkShorter,LinkShorterStrategy
import requests
import bitlyshortener
from shorty.errors import APIError
import os



def shortLink(request):
    url = request["url"]
    if "provider" in request:
        provider = request["provider"]
        if provider == ShorthenLinkType.BITLY.value:
            linkShorterProvider = LinkShorter(BitlyLinkShorter())      
        elif provider == ShorthenLinkType.TINYURL.value:
            linkShorterProvider = LinkShorter(TinyLinkShorter())
        link = linkShorterProvider.use_provider(url)
        return link    
    else:
        linkShorterProvider = LinkShorter(BitlyLinkShorter())
        link = linkShorterProvider.use_providers(url,
        [LinkShorter(TinyLinkShorter()),
        ]
        )
        return link


# This class provides utility functions for shorthen an url with provider https://dev.bitly.com/
# 1. short_link(self,url): returns the short version of the url by https://dev.bitly.com/ with using library named bitlyshortener
class BitlyLinkShorter(LinkShorterStrategy):
    
    def short_link(self,url):
        try:
            access_tokens = [os.environ.get("BITLY_ACCESS_TOKEN")] 
            shortener = bitlyshortener.Shortener(tokens=access_tokens)  
            long_urls= shortener.shorten_urls([url])
        except:
            raise APIError(503,"Bitly service unavailable")  
        return long_urls[0]

# This class provides utility functions for shorthen an url with provider https://gist.github.com/MikeRogers0/2907534
# 1. short_link(self,url): returns the short version of the url by https://gist.github.com/MikeRogers0/2907534
class TinyLinkShorter(LinkShorterStrategy):
    def short_link(self,url):
        payload = {"url": url}
        response = requests.get("http://tinyurl.com/api-create.php", params=payload)
        if response.status_code == 200:
            return response.text
        else:
            raise APIError(500,"Tinyurl provider returns error")
     