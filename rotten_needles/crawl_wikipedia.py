"""Generate movie title files from Wikipedia."""

import os

import urllib.request
from bs4 import BeautifulSoup as bs

from .shared import TITLES_DIR_PATH


def _extract_titles(movie_table):
    rows = movie_table.find_all('tr')
    content = []
    for row in rows:
        content.append([td.get_text() for td in row.find_all(["td", "th"])])
    titles = []
    for row in content:
        if len(row) == 6:
            titles.append(row[0])
        elif len(row) == 7:
            titles.append(row[1])
        elif len(row) == 8:
            titles.append(row[2])
        else:
            print("unknown length!")
            print(row)
    return titles


def _extract_titles_from_wiki_page(wiki_url):
    wiki_page = bs(urllib.request.urlopen(wiki_url), "html.parser")
    movies_tables = wiki_page.find_all('table', {'class': 'wikitable'})
    titles = []
    for table in movies_tables:
        print("Extracting a table...")
        titles += _extract_titles(table)
    titles = [title for title in titles if title != "Title"]
    print('{} titles collected.'.format(len(titles)))
    return titles


def _title_list_to_title_file(title_list, year):
    file_path = os.path.join(TITLES_DIR_PATH, '{}_titles.txt'.format(year))
    with open(file_path, 'w+') as titles_file:
        titles_file.write('\n'.join(title_list))


URL_MAP_BY_YEAR = {
    2014: 'https://en.wikipedia.org/wiki/List_of_American_films_of_2014',
    2015: 'https://en.wikipedia.org/wiki/List_of_American_films_of_2015',
}

def generate_title_files():
    """Generate movie title files from Wikipedia."""
    print("Generate movie title files from Wikipedia...")
    titles_by_year = {}
    for year in URL_MAP_BY_YEAR:
        print("For year {}...".format(year))
        titles_by_year[year] = _extract_titles_from_wiki_page(
            URL_MAP_BY_YEAR[year])
        _title_list_to_title_file(titles_by_year[year], year)
