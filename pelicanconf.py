#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import fontawesome as fa

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

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/geoponge', ':fa:`fa-twitter`'),('github', 'https://github.com/chunnodu', ':fa:`fa-github`'),('linkedin', 'https://www.linkedin/in/chunnodu', ':fa:`fa-linkedin`'))
# 'mailto:chuknnodu@gmail.com')

GITHUB_URL = 'https://github.com/chunnodu'
TWITTER_USERNAME = 'https://twitter.com/geoponge'

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Enable Pelican FontAwesome icons
#PLUGIN_PATH = 'plugins'
PLUGINS = ['tipue_search','pelican_fontawesome']
#DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']