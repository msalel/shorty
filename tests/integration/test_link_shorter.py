
def test_short_link_without_provider(post):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/shortlinks' endpoint is posted to (POST)
    THEN check the response is valid
    """

    response = post('/shortlinks',data=dict(url='https://www.google.com'))

    assert response.status_code == 200
    assert b'https://bit.ly' in response.data

def test_short_link_with_provider(post):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/shortlinks' endpoint is posted to (POST)
    THEN check the response is valid
    """

    response = post('/shortlinks',data=dict(url='https://www.google.com',provider='TINYURL'))

    assert response.status_code == 200
    assert b'https://tinyurl.com/' in response.data 

    
