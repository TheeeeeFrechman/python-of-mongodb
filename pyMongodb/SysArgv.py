#!/usr/bin/python
# -*- coding: utf-8 -*-  

from xml.etree import ElementTree
import storage

class SysArgv(object):
    def __init__(self):
        conffile = '/CySec_H008/conf/SysSet.xml'
        tree = ElementTree.ElementTree(file = conffile)
        root = tree.getroot()

        node = root.find('out_device')
        self.DEVICE = storage.DEVICE_TYPE.DEVICE_MONGO
        if node is None:
            print 'There is no a node named out_device in the conf file: %s' % (conffile)
        else:
            self.DEVICE = int(node.text)

        node = root.find('auth_type')
        self.AUTH_TYPE = '03'
        if node is None:
            print 'There is no a node named out_device in the conf file: %s' % (conffile)
        else:
            self.AUTH_TYPE = node.text