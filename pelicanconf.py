#!/usr/bin/env python
# -*- coding: utf-8 -*- 


AUTHOR = 'Chu Nnodu'

GITHUB_URL = 'https://github.com/chunnodu'
PATH = 'content'
SITENAME = 'Chu\'s Digital Log'
#SITEURL = 'http://localhost:8000'

THEME = "pelican-minimal"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'notes'

SUMMARY_MAX_LENGTH = 20

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

#DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']