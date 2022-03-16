from shorty.service.link_shorter_service import shortLink
from shorty.model.link_shorter_model import providerValidate
from marshmallow import ValidationError


def test_short_link_with_provider():
    """
    GIVEN request as dict with both variables
    WHEN shortLink function called
    THEN check the returned value is valid
    """
    request = dict(url="https://www.google.com",provider="TINYURL")
    link = shortLink(request)
    assert  link.startswith('https://tinyurl.com/' )
    assert not link.startswith('https://bit.ly' )

def test_short_link_without_provider():
    """
    GIVEN request as dict without provider
    WHEN shortLink function called
    THEN check the returned value is valid
    """
    request = dict(url="https://www.google.com")
    link = shortLink(request)
    assert  link.startswith('https://bit.ly' )


def test_provider_validater():
    """
    GIVEN provider type
    WHEN providerValidate function called
    THEN check the returned value raised an error
    """
    try:
        providerValidate("BITLY")
    except ValidationError as verr:
        assert False, f"'BITLY' raised an exception {verr}"
