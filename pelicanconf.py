#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ian Sullivan'
SITENAME = u'edtechgarden'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'pelicanoutput'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

MENUITEMS = [('Help us build on github!','https://github.com/edtechgarden/edtechgarden.github.io')]

THEME = "themes/nest"
NEST_HEADER_LOGO = '/images/1by.png'
NEST_SITEMAP_MENU = [('Help us build on github!','https://github.com/edtechgarden/edtechgarden.github.io')]
GITHUB_URL = "https://github.com/edtechgarden/edtechgarden.github.io"

# This kills some of the default navigation pages since we are building our own
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
INDEX_SAVE_AS = ''

ARTICLE_SAVE_AS = "{category}/{slug}.html"
PAGE_SAVE_AS = "{category}/{slug}.html"
DISPLAY_PAGES_ON_MENU = False
TYPOGRIFY = True


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

# Social widget

DEFAULT_PAGINATION = 10

## The following options are useful for build testing but can be dangerous

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Should you delete the contents of the output dir with each build?
DELETE_OUTPUT_DIRECTORY = False