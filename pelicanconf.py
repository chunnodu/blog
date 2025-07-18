#!/usr/bin/env python
# -*- coding: utf-8 -*- 


AUTHOR = 'Chu Nnodu'


SITENAME = 'Chu\'s Digital Log'
#SITEURL = 'http://localhost:8000'

PATH = 'content'

THEME = './themes/voce/' 

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'notes'

SUMMARY_MAX_LENGTH = 15


# Blogroll
LINKS = (('Blog', 'https://chunnodu.com/tag/reading.html'),
         ('Top Skills', 'https://secure.plum.io/p/o93Pr7IyMGN98jHG9suN5A'),
         ('Projects', './output/projects.html')
         )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/ajaredia'), 
        ('Linkedin', 'https://linkedin.com/in/chunnodu'), 
              ('Github', 'https://github.com/chunnodu'))


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing

RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives']

# Display Submenu with article categories

#TAGS_URL = 'tags.html'
#ARCHIVES_URL = 'archives.html'
CATEGORY_URL = 'categories.html'

USER_LOGO_URL = 'https://chunnodu.com/images/chunnodu.png'

DISPLAY_PAGES_ON_MENU = False

INDEX_SAVE_AS = 'blog/index.html'  # Moves blog roll to /blog/
ARTICLE_URL = 'blog/{slug}.html'   # Blog posts go under /blog/
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'           # Static pages keep simple URLs
PAGE_SAVE_AS = '{slug}.html'


# Take all article urls under posts
#ARTICLE_URL = "posts/{date:%Y}-{date:%m}-{date:%d}-{slug}.html"
#ARTICLE_SAVE_AS = "posts/{date:%Y}-{date:%m}-{date:%d}-{slug}.html"

#ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
#ARTICLE_URL = '{date:%Y}/{slug}.html'


# Take all index file under posts
#INDEX_SAVE_AS = 'posts/index.html'
#INDEX_URL = 'posts/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

