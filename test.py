#!python
# -*- coding=utf8 -*-

import unittest
from run import xml2dicts, getlength, findLengthFromHTML



class TestCase_findLengthFromHTML(unittest.TestCase):
  def test_K3tgOwAACAAJ(self):
    f = open('K3tgOwAACAAJ.html')
    n = findLengthFromHTML(f)
    self.assertEqual(n, 519)

  def test__lKUQgAACAAJ(self):
    f = open('-lKUQgAACAAJ.html')
    n = findLengthFromHTML(f)
    self.assertEqual(n, 413)


class TestCase_getlength(unittest.TestCase):
  def setUp(self):
    pass

  def test_K3tgOwAACAAJ(self):
    pass





class TestCase_xml2dicts(unittest.TestCase):
  def setUp(self):
    pass

  def testmulti(self):
    '''multiple.xml contains three books'''
    iter = xml2dicts('multi.xml')
    self.assertEqual(iter[0], 
      {
        'id':'-lKUQgAACAAJ', 
        'url':'http://books.google.com/books?id=-lKUQgAACAAJ', 
        'title':'Dive into Python', 
        'contributor':'Mark Pilgrim', 
        'isbn':'1590593561', 
        'length':413,
      }
    )
    self.assertEqual(iter[1], 
      {
        'id':'K3tgOwAACAAJ', 
        'url':'http://books.google.com/books?id=K3tgOwAACAAJ',
        'title': u'開発のプロが教える標準Django完全解説', 
        'contributor': u'増田泰, 中居良介, 露木誠, 松原豊',
        'isbn': '4048672096',
         'length': 519,
      }
    )
    self.assertEqual(iter[2], 
      {
        'id':'RgvFQgAACAAJ',
        'url':'http://books.google.com/books?id=RgvFQgAACAAJ', 
        'title':'wxPython in action', 
        'contributor':'Noel Rappin, Robin Dunn',
        'isbn':'1932394621', 
        'length':552,
      }
    )
    self.assertEqual(len(iter), 3)

  def testsingle(self):
    '''single.xml contains a book'''

    iter = xml2dicts('single.xml')

    self.assertEqual(iter[0], 
      {
        'id':'rsBdPgAACAAJ',
        'url': 'http://books.google.com/books?id=rsBdPgAACAAJ', 
        'title': u'Django×Python',
        'contributor': u'露木誠',
        'isbn': '477413760X', 
        'length': 287, 
      }
    )
    self.assertEqual(len(iter), 1)

