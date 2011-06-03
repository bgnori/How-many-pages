#!python
# -*- coding=utf8 -*-

from xml.etree.ElementTree import *


tree = parse('single.xml')
root = tree.getroot()


ve = root.find('.//identifier/value')
print ve.text #isbn, #477413760X


def xml2dicts(input):
  '''Returns list of dicts, every dict holds data on a book.'''

  m = [
    {
      'id':'K3tgOwAACAAJ', 
      'url':'http://books.google.co.jp/books?id=K3tgOwAACAAJ',
      'title': u'開発のプロが教える標準Django完全解説', 
      'contributor': u'増田泰, 中居良介, 露木誠, 松原豊',
      'isbn': '4048672096', 'page': 519
    },
    {
      'id':'-lKUQgAACAAJ', 
      'url':'http://books.google.co.jp/books?id=-lKUQgAACAAJ', 
      'title':'Dive into Python', 
      'contributor':'Mark Pilgrim', 
      'isbn':'1590593561', 
      'page':413
    },
    {
      'id':'RgvFQgAACAAJ',
      'url':'http://books.google.co.jp/books?id=RgvFQgAACAAJ', 
      'title':'wxPython in action', 
      'contributor':'Noel Rappin, Robin Dunn',
      'isbn':'1932394621', 
      'page':552
    }
  ]
  s = [
    {'isbn': '477413760X', 
     'id':'sBdPgAACAAJ',
     'url': 'http://books.google.co.jp/books?id=rsBdPgAACAAJ', 
     'page': 287, 
     'title': u'Django×Python'
    }
  ]
  return s

if __name__ == '__main__':
  print 'testing'
  doctest.testmod()

