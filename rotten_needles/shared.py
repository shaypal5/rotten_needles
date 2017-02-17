"""Shared resources for the Rotten Needles package."""

import os

HOMEDIR = os.path.expanduser("~")
IMDB_SUBPACKAGE_PATH = os.path.dirname(os.path.realpath(__file__))
PACKAGE_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
IMDB_SUBPACKAGE_PATH = os.path.join(PACKAGE_DIR_PATH, 'imdb_crawl')
REPO_DIR_PATH = os.path.dirname(PACKAGE_DIR_PATH)
DATA_DIR_PATH = os.path.join(REPO_DIR_PATH, 'data')
PROFILES_DIR_PATH = os.path.join(DATA_DIR_PATH, 'movie_profiles')
TITLES_DIR_PATH = os.path.join(DATA_DIR_PATH, 'title_lists')
