#!python
# -*- coding=utf8 -*-

from xml.etree.ElementTree import *

def getpage(url):
  '''Returns number of pages from google books.'''
  map = {
    'http://books.google.com/books?id=K3tgOwAACAAJ': 519,
    'http://books.google.com/books?id=-lKUQgAACAAJ': 413,
    'http://books.google.com/books?id=RgvFQgAACAAJ': 552,
    'http://books.google.com/books?id=rsBdPgAACAAJ': 287,
  }

  return map[url]

TAGS = {'id':None, 'url':None, 'title':None, 'contributor':None, 'isbn':None,}

def xml2dicts(input):
  '''Returns list of dicts, every dict holds data on a book.'''
  
  tree = parse(input)
  root = tree.getroot()
  books = root.find('.//books')
  result = []
  for book in books.findall('./book'):
    d = dict(TAGS)
    for elem in book.getchildren():
      if elem.tag in TAGS:
        d[elem.tag] = elem.text
      elif elem.tag == 'identifier':
        d['isbn'] = elem.find('./value').text
    d['length'] = getpage(d['url'])
    result.append(d)
  return result

if __name__ == '__main__':
  pass
