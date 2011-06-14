#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
list-bookmarks.py
~~~~~~~~~~~~~~~~~

This module is an example of how to harness the Readability API w/ oAuth.

This module expects the following environment variables to be set:

- READABILITY_CONSUMER_KEY
- READABILITY_CONSUMER_SECRET
- READABILITY_OAUTH_TOKEN
- READABILITY_OAUTH_SECRET

Once you have your consumer keys setup, run the following to get your OAuth
tokens::

    $ ./login.py <username> <password>

"""


import sys

from ext import readability
from ext import get_consumer_keys, get_oauth_token


USAGE = """
Usage:

   $ ./login.py <username> <password>
"""

TEMPLATE = """
To use the other example modules, run the following:

  $ export READABILITY_OAUTH_TOKEN=%s
  $ export READABILITY_OAUTH_SECRET=%s
"""


def main():

    try:
        c_key, c_secret = get_consumer_keys()
    except ValueError:
        print >> sys.stderr, 'READABILITY_OAUTH_TOKEN and READABILITY_OAUTH_SECRET must be set.'
        sys.exit(1)

    token = get_oauth_token()

    rdd = readability.oauth(c_key, c_secret, token=token)

    # print rdd.get_bookmarks(user='kreitz')
    bookmarks = rdd.get_me().bookmarks()

    for mark in bookmarks:
        print '- %s (%s)' % (mark.article.title, mark.article.domain)


if __name__ == '__main__':
    main()