#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Chu Nnodu'
SITENAME = 'Chu's Digital Log'
SITEURL = 'https://chunnodu.com'

PATH = 'content'

THEME = 'themes/pelican-minimal'

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

# Social widget
#SOCIAL = (Twitter, 'https://twitter.com/geoponge',<i class="fab fa-twitter"></i>)
#         (Github, 'https://github.com/chunnodu',<i class="fab fa-github"></i>)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}