#!/usr/bin/python
'''
    @File        singleton.py
    @Author      pengsen cheng
    @Company     bhyc
    @CreatedDate 2014-07-03
'''

def singleton(cls, *args, **kw):  
    instances = {}  
    def _singleton():  
        if cls not in instances:  
            instances[cls] = cls(*args, **kw)  
        return instances[cls]  
    return _singleton  
