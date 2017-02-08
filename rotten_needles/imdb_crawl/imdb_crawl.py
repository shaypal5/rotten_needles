"""Crawls and extracts choice metrics from IMDB movie profiles."""

from urllib.request import urlopen

from bs4 import BeautifulSoup as bs

TITLE_QUERY = (
    'http://www.imdb.com/find'
    '?q={title}&s=tt&ttype=ft&exact=true&ref_=fn_tt_ex'
)


def get_basic_movie_profile(movie_name):
    """Returns a basic profile for the given movie."""
    query = TITLE_QUERY.format(title=movie_name)
    search_res = bs(urlopen(query), "html.parser")
