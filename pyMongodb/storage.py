#!/usr/bin/python
# -*- coding: utf-8 -*-  


from mongodb import mongo_interface
from SysArgv import SysArgv
from opcode import *
from tools import MemCache

class DEVICE_TYPE(object):     
    DEVICE_SYS   = 0x80000000
    DEVICE_MONGO = 0x00000001


argv = SysArgv() 

def DAInsert(table, data, type, safe_on = False): 
    
    tag = DO_ERROR_INVALID
    mask = ((type & DEVICE_TYPE.DEVICE_SYS) == DEVICE_TYPE.DEVICE_SYS) and (argv.DEVICE | (type & 0x7fffffff)) or type

    if (mask & DEVICE_TYPE.DEVICE_MONGO) == DEVICE_TYPE.DEVICE_MONGO:
        tag = mongo_interface.insert_into_mongo(table, data, safe_on)
    
    return tag

def DAQuery(table, con, sort, field, skip, limit, type):
    return mongo_interface.find_from_mongo(table, con, sort, field, skip, limit)

def DAUpdate(table, con, value, type):
    return mongo_interface.update_from_mongo(table, con, value, False)

def DADelete(table, con, type):
    return mongo_interface.delete_from_mongo(table, con)
    
def DAReplace(table, con, value, type):
    return mongo_interface.update_from_mongo(table, con, value, True)

def DA_UpdateGIS(auth, x, y, street, capture_time):
    return mongo_interface.update_gis_from_mongo(auth, x, y, street, capture_time)

def DA_IP2Auth(ip, port, mac):
    return mongo_interface.get_auth_from_mongo_by_ip(ip, port, mac, argv.AUTH_TYPE)

def DA_Auth2IP(auth_type, auth):
    return mongo_interface.get_ip_from_mongo_by_auth(auth_type, auth)

def DA_Auth2GIS(auth):
    return mongo_interface.get_gis_from_mongo_by_auth(auth)

def DA_IsCatche(key):
    mc = MemCache()
    return mc.isexist(key)

def DA_SetCatche(key, seconds):
    mc = MemCache()
    mc.set(key, seconds)

def DA_DelInsert(table, con, data, type):
    return mongo_interface.delete_and_insert(table, con, data)
