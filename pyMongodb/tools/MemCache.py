#!/usr/bin/python
# -*- coding: utf-8 -*-  

import memcache
from xml.etree import ElementTree
import traceback
from singleton import singleton

@singleton
class MemCache(object):
    def __init__(self):
        conffile = '/item/conf/SysSet.xml'
        tree = ElementTree.ElementTree(file = conffile)
        root = tree.getroot()
        node = root.find('webserver') 
        if node is None:
            print 'There is no a node named database in the conf file: %s' % (conffile)
            sys.exit(1)

        try:
            ip = node.text + ':22121'
            self.__mc = memcache.Client([ip], debug = 0)
        except Exception, e:
            print traceback.print_exc()
            self.__mc = None
        
    def set(self, key, seconds):
        if self.__mc is not None:
            try:
                self.__mc.set(key, '1', seconds)
            except Exception, e:
                print traceback.print_exc()
    
    def isexist(self, key):
        if self.__mc is not None:
            try:
                if self.__mc.get(key) is not None:
                    return True
                else:
                    return False 
            except Exception, e:
                print traceback.print_exc()
                return False
