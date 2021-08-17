from web_scraper import __version__
from web_scraper.scraper import *

def test_version():
    assert __version__ == '0.1.0'


def test_get_citations_needed_count():
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    actual = get_citations_needed_count(url)
    expected = 5
    assert expected == actual

def test_get_citations_needed_report():
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    actual = get_citations_needed_report(url)
    expected = str(get_citations_needed_report(url))
    assert expected == actual 
