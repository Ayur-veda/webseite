#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yogi'
SITENAME = u'Ayur-Veda'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'de'
DEFAULT_CATEGORY = 'Verschiedenes'
STATIC_PATHS = ['Bilder']
PAGE_PATHS= ['Seiten']
TYPOGRIFY = True
PLUGIN_PATHS = ['/Users/axel/src/Pelican/pelican-plugins/assets']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# THEME = "/Users/axel/src/Pelican/pelican-themes/brownstone"
# THEME = '/Users/axel/src/Pelican/pelican-themes/Nuja'
THEME = '/Users/axel/src/Pelican/pelican-themes/plumage'

