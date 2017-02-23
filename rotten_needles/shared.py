"""Shared resources for the Rotten Needles package."""

import os
import re

HOMEDIR = os.path.expanduser("~")
IMDB_SUBPACKAGE_PATH = os.path.dirname(os.path.realpath(__file__))
PACKAGE_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
IMDB_SUBPACKAGE_PATH = os.path.join(PACKAGE_DIR_PATH, 'imdb_crawl')
REPO_DIR_PATH = os.path.dirname(PACKAGE_DIR_PATH)
DATA_DIR_PATH = os.path.join(REPO_DIR_PATH, 'data')
PROFILES_DIR_PATH = os.path.join(DATA_DIR_PATH, 'movie_profiles')
TITLES_DIR_PATH = os.path.join(DATA_DIR_PATH, 'title_lists')
METACRITIC_DIR_PATH = os.path.join(DATA_DIR_PATH, 'metacritic_profiles')


class _result:
    SUCCESS = 'succeeded'
    FAILURE = 'failed'
    EXIST = 'already exist'
    ALL_TYPES = [SUCCESS, FAILURE, EXIST]


def _file_length(file_path):
    length = 0
    with open(file_path, 'r') as movies_file:
        for line in movies_file:
            length += 1
    return length


CHARS_TO_REMOVE = r"[\:\;,\.'/\!]"

def _parse_name_for_file_name(movie_name):
    parsed = re.sub(CHARS_TO_REMOVE, '', movie_name)
    return parsed.replace(' ', '_').lower()
