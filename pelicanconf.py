#!/usr/bin/env python
# -*- coding: utf-8 -*- 


AUTHOR = 'Chu Nnodu'

GITHUB_URL = 'https://github.com/chunnodu'
PATH = 'content'
SITENAME = 'Chu\'s Digital Log'
#SITEURL = 'http://localhost:8000'

THEME = "./themes/voce"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'notes'

SUMMARY_MAX_LENGTH = 15

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('About', 'https://chunnodu.com/pages/me.html'),
         ('Projects', 'https://chunnodu.com/pages/projects.html'),
         ('Top Skills', 'https://secure.plum.io/p/o93Pr7IyMGN98jHG9suN5A')
         )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/geoponge'), 
        ('Linkedin', 'https://linkedin.com/in/chunnodu'), 
              ('Github', 'https://github.com/chunnodu'))


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

#DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']

# Display Submenu with article categories

TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archives.html'
CATEGORY_URL = 'categories.html'

USER_LOGO_URL = './output/images/chunnodu.png'

DISPLAY_PAGES_ON_MENU = True