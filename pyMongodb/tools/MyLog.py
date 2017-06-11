#!/usr/bin/python
# -*- coding: utf-8 -*-  
'''
    @File        MyLog.py
    @Author      pengsen cheng
    @Company     bhyc
    @CreatedDate 2014-04-02
'''

import time, sys, os
reload(sys) 
sys.setdefaultencoding('utf-8')
from singleton import singleton

@singleton
class MyLog(object):
    '''
    this class is bulid for logging the running information. it can creates the
    log file by time. one day's log informtion recodes in a log file.
        
    Attributes:
        __handle: log file handle.
        __time: String, format likes YYYYMMDD
    
    __authors__ = [
    'pengsen cheng'
    ]
    '''
    __handle = None
    __time = ''
    __path = None
    def __init__(self, path='/CySec_H008/log/storage'):
        '''
        construction function. to open the log file, and changes the file
        when the time is changed.
        Args:
            path: string, the log file's path
        Returns:
            None
        Raises:
            None.
        '''
        #the time in the file name likes YYYYMMDD
        now = time.strftime('%Y%m%d', time.localtime(time.time()))
        
        #save the new time 
        MyLog.__time = now
        MyLog.__path = path
        #bulid the file name liks path/pYYYYMMDD.log
        filename = MyLog.__path + '/py-' + now + '.log'
        try:
            MyLog.__handle = open(filename, 'a')
        except Exception, ex:
            print 'Exception' + ':' + str(ex)
        
    
    def __del__(self):
        '''
        destruction function. to close the log file.
        
        Args:
            path: string, the log file's path.
        Returns:
            None
        Raises:
            None.
        '''
        if self.__class__.__handle is not None:
            self.__class__.__handle.close()
            self.__class__.__handle = None
    
    def write(self, format, args = None):
        '''
        to record the user's data to the log file.
        
        Args:
            format: string, the final format of the use's data.
            args: tuple, the parts of the format are needed to replace 
        Returns:
            None.
        Raises:
            None.
        '''
        now = time.strftime('%Y%m%d', time.localtime(time.time()))
        if now != MyLog.__time:
            MyLog.__time = now
            MyLog.__handle.close()
            filename = MyLog.__path + '/py-' + now + '.log'
            try:
                MyLog.__handle = open(filename, 'a')
            except Exception, ex:
                print 'Exception' + ':' + str(ex)
        
        now = time.strftime('[%H:%M:%S]', time.localtime(time.time()))
        line = ''
        if args is None:
            line = format
        else:
            line = format % args
            
        MyLog.__handle.write(now + line)
        MyLog.__handle.flush()
        os.fsync(MyLog.__handle.fileno())
        
       
