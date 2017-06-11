#!/usr/bin/python
'''
    @File        opcode.py
    @Author      pengsen cheng
    @Company     bhyc
    @CreatedDate 2014-04-03
'''

class _opcode(object):
    class ConstError(TypeError):
        pass
    
    def __init__(self):
        self.__dict__['DO_SUCCESS'] = 0
        self.__dict__['DO_UNSUCCESS'] = -1
        self.__dict__['DO_OK'] = -2
        self.__dict__['DO_ERROR_SQL'] = -3
        self.__dict__['DO_ERROR_KEY'] = -4
        self.__dict__['DO_ERROR_INVALID'] = -5
        self.__dict__['DO_ERROR_REPAIR'] = -6
        self.__dict__['DO_ERROR_RKEY'] = -7
        self.__dict__['DO_ERROR_UN'] = -8
        self.__dict__['DO_ERROR_OPEN'] = -9
    
    def __setattr__(self,name,value):
        if self.__dict__.has_key(name):
            raise self.ConstError,"Can't rebind const (%s)" % name
        self.__dict__[name] = value
        
import sys 
sys.modules[__name__] = _opcode()

