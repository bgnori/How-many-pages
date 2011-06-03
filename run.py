#!python
# -*- coding=utf8 -*-

import re
import urllib2
from xml.etree.ElementTree import *

LENGTHPATTERN = r'''<tr class="metadata_row"><td class="metadata_label">Length</td><td class="metadata_value"><span dir=ltr>(?P<length>\d+) pages</span></td></tr>'''

REGEXP = re.compile(LENGTHPATTERN)

def hackCookie(fn):
  f = open(fn)
  try:
    return f.read()[len('Cookie: '):]
  finally:
    f.close()

opener = urllib2.build_opener()
opener.addheaders = [('Cookie', hackCookie('cookie.txt'))]


def findLengthFromHTML(html):
  text = html.read()
  m = REGEXP.search(text)
  return int(m.groupdict()['length'])


def getlength(url):
  '''Returns number of pages from google books.'''
  h = opener.open(url)
  try:
    return findLengthFromHTML(h)
  finally:
    h.close()

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
        d[elem.tag] = elem.text.encode('utf-8')
      elif elem.tag == 'identifier':
        d['isbn'] = elem.find('./value').text.encode('utf-8')
    d['length'] = getlength(d['url'])
    result.append(d)
  return result

if __name__ == '__main__':
  import sys
  import csv
  import codecs

  in_file = sys.argv[1]
  
  print in_file
  out_file = in_file[:-3] + 'csv'
  print out_file
  
  ds = xml2dicts(in_file)

  out = open(out_file, 'wb') 
  writer = csv.DictWriter(out, ['isbn', 'title', 'length'], restval='', extrasaction='ignore')
  writer.writerows(ds)
  out.close()
  
 

