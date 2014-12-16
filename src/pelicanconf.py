# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Clint Savage'
SITENAME = u'Uptime SLC'
SITEURL = 'http://uptimeslc.org'
SITESUBTITLE = u'A gathering of system administrators and technology enthusiasts'

TIMEZONE = 'America/Denver'
INDEX_WELCOME = u'Welcome to Uptime SLC'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Utah Open Source', 'http://utos.org/'),
          ('Utah Python', 'http://utahpython.org/'),
          )


THEME = 'themes/Just-Read'
# Social widget
#SOCIAL = ''

DEFAULT_PAGINATION = 5
DELETE_OUTPUT_DIRECTORY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

INDEX_SAVE_AS = 'index.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

#DELETE_OUTPUT_DIRECTORY = True

DISPLAY_CATEGORIES_ON_MENU = False
REVERSE_CATEGORY_ORDER = True
DEFAULT_DATE = 'fs'
DEFAULT_CATEGORY = 'Community'
