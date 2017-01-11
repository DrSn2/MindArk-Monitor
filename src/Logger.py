#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 11 jan. 2017

@author: Fredrick
'''

import DBConnection
from DBConnection import *
from time import gmtime, strftime

class Logger(object):
    '''
    Has functions for logging activity. 
    Use write() for default behaviour.
    '''


    def __init__(self, args, conf):
        '''
        Constructor
        '''
        self.logFile = None
        self.db = DBConnection(args, conf)
    
    def write(self, message):
        """ Default log function """
        if (not self.writeToDB(message)):
            self.writeToFile(message)
    
    def writeToDB(self, message):
        """ Writes message into the database """
        if (not self.db.writeLog(message)):
            return False
        
        return True
    
    def writeToFile(self, message):
        """ Writes message into a file """
        dt = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        self.logFile = open("log.txt", "a")
        self.logFile.write(dt + '\t' + message)
        self.logFile.close()