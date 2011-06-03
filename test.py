#!python
# -*- coding=utf8 -*-

import unittest
from run import xml2dicts



class TestCaseForxml2dicts(unittest.TestCase):
  def setUp(self):
    pass

  def testmulti(self):
    '''multiple.xml contains three books'''
    f = open('multi.xml')
    iter = xml2dicts(f)
    self.assertEqual(iter[0], 
      {
        'id':'K3tgOwAACAAJ', 
        'url':'http://books.google.co.jp/books?id=K3tgOwAACAAJ',
        'title': u'開発のプロが教える標準Django完全解説', 
        'contributor': u'増田泰, 中居良介, 露木誠, 松原豊',
        'isbn': '4048672096', 'page': 519
      }
    )
    self.assertEqual(iter[1], 
      {
        'id':'-lKUQgAACAAJ', 
        'url':'http://books.google.co.jp/books?id=-lKUQgAACAAJ', 
        'title':'Dive into Python', 
        'contributor':'Mark Pilgrim', 
        'isbn':'1590593561', 
        'page':413
      }
    )
    self.assertEqual(iter[2], 
      {
        'id':'RgvFQgAACAAJ',
        'url':'http://books.google.co.jp/books?id=RgvFQgAACAAJ', 
        'title':'wxPython in action', 
        'contributor':'Noel Rappin, Robin Dunn',
        'isbn':'1932394621', 
        'page':552
      }
    )
    f.close()

  def testsingle(self):
    f = open('single.xml')
    iter = xml2dicts(f)

    self.assertEqual(iter[0], 
      {
        'isbn': '477413760X', 
        'id':'sBdPgAACAAJ',
        'url': 'http://books.google.co.jp/books?id=rsBdPgAACAAJ', 
        'page': 287, 
        'title': u'Django×Python'
      }
    )
    f.close()
