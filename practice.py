#!/usr/bin/env python
# encoding: UTF-8
# 'makeTextFile.py -- create text file'
#
# import os
# ls = os.linesep
#
# #get filename
# while True:
#     fname = raw_input('Enter filename:')
#     if os.path.exists(fname):
#         print "ERROR: '%s' already exists" % fname
#     else:
#         break
#
# # get file content (text) lines
# all = []
# print "\nEnter lines('.' by itself to quit).\n"
#
# # loop until user terminates input
# while True:
#     entry = raw_input('>')
#     if entry == '.':
#         break
#     else:
#         all.append(entry)
#
# # write lines to file with proper line-ending
# fobj = open(fname, 'w')
# fobj.writelines(['%s%s' % (x, ls) for x in all])
# fobj.close()
# print 'DONE!'

#!/usr/bin/env Python

'readTextFile.py -- read and display text file'

#get filename
# fname = raw_input('Enter filename:')
# #print
# #attempt to open file for reading
# try:
#     fobj = open(fname, 'r')
# except IOError, e:
#     print '*** file open error:', e
# else:
#     #display contents to the screen
#     for eachLine in fobj:
#         print eachLine,
#     fobj.close()

# s = 'abcde'
# for i in range(1,len(s)+1):
#     print i
#     print s[:i]

# queue = []
# aTuple = (123,)
# def enQ():
#     queue.append(raw_input('Enter new string:').strip())
#     print queue
#
# def deQ():
#     if len(queue) == 0:
#         print 'Cannot pop from an empty queue!'
#     else:
#         print 'Removed [', 'queue.pop(0) ',' ]'
#
# def viewQ():
#     print queue
#
# CMDs = {'e': enQ, 'd':deQ, 'v':viewQ}
#
# def showmenu():
#     pr = """"
#     (E)nqueue
#     (D)equeue
#     (V)iew
#     (Q)uit
#
#
#     Enter choice"""
#
# print aTuple

# 浅拷贝
# person = ['name', ['savings', 100.00]]
# hubby = person[:]
# wifey = list(person)
# print [id(x) for x in person, hubby, wifey]
# hubby[0] = 'joe'
# wifey[0] = 'james'
# print hubby, wifey
# hubby[1][1] = 50.00
# print hubby, wifey
# all = []
# while True:
#     a = raw_input('enter a number')
#     if a.isdigit() or a == '.':
#         if a == '.':
#             break
#         else:
#             all.append(int(a))
#     else:
#         continue
# all.sort()
# print all

# max line
# f = open('/etc/motd', 'r')
# allLineLens = [len(x.strip()) for x in f]
# f.close()
# print max(allLineLens)
# class MyClass(object):
#     'Myclass class definition'
#     myVersion = '1.1'
#     def showVersion(self):
#         print MyClass.myVersion
#
# mc = MyClass()
# print MyClass.__name__
# print MyClass.__module__
# print type(mc)

# from os import popen
# from re import split
#
# f = popen('who','r')
# for eachLine in f:
#     print split('\s\s+|\t', eachLine.strip())
# f.close()

import random
from string import lowercase
from sys import maxint
from time import ctime

doms = ('com', 'edu', 'net', 'org', 'gov')

for i in range(random.randint(5, 10)):
    random.randint(0, maxint -1)
    ctime()