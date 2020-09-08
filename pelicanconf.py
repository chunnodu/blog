#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Chu Nnodu'
SITENAME = 'Digital Log'
SITEURL = 'http://localhost:8000'

PATH = 'content'

THEME = 'pelican-minimal'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('You can add links in your config file', 'https://twitter.com/geoponge'),
          ('Another social link', 'https://github.com/chunnodu'),)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True