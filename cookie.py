#!python
# -*- coding=utf8 -*-

import urllib2

url = 'http://books.google.com/books?id=rsBdPgAACAAJ'

opener = urllib2.build_opener()

f = open('cookie.txt')
COOKIE = f.read()[len('Cookie: '):]


opener.addheaders = [('Cookie', COOKIE)]
h = opener.open(url)
print h.info()
print h.read()[:200]


