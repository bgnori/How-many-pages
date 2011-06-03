#!python
# -*- coding=utf8 -*-

import doctest
from xml.etree.ElementTree import *


tree = parse('single.xml')
root = tree.getroot()


ve = root.find('.//identifier/value')
print ve.text #isbn, #477413760X


def xml2dicts(input):
  '''
  >>> f = open('single.xml')
  >>> iter = xml2dicts(f)
  >>> d = iter[0]
  >>> d
  {'isbn': '477413760X', 'page': 287, 'title': ''' + repr(u'Django×Python')  + \
  ''', 'url': 'http://books.google.co.jp/books?id=rsBdPgAACAAJ', 'id':'sBdPgAACAAJ'}
    
  '''
  return [
            {'isbn': '477413760X', 
             'id':'sBdPgAACAAJ',
             'url': 'http://books.google.co.jp/books?id=rsBdPgAACAAJ', 
             'page': 287, 
             'title': u'Django×Python'}
        ]

if __name__ == '__main__':
  print 'testing'
  doctest.testmod()

