#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = '3d expo team'
SITENAME = '3D EXPO'
SITEURL = '3d-expo.co.uk'

SITETITLE = '3D Expo - Inspiration to create things for enthusiasts'


PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Plugins
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ['related_posts', 'series', 'sitemap', 'tag_cloud', 'assets', 'share_post']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "themes/neat"
