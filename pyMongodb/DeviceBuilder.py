#!/usr/bin/python
# -*- coding: utf-8 -*-  

from xml.etree import ElementTree
import storage

class DeviceBuilder(object):
    def __init__(self):
        conffile = '/item/conf/SysSet.xml'
        tree = ElementTree.ElementTree(file = conffile)
        root = tree.getroot()
        node = root.find('out_device')
        self.DEVICE = storage.DEVICE_TYPE.DEVICE_MONGO
        
        if node is None:
            print 'There is no a node named out_device in the conf file: %s' % (conffile)
        else:
            self.DEVICE = int(node.text)
