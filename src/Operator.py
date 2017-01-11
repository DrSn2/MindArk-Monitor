#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 11 jan. 2017

@author: Fredrick
'''

import Logger
from Logger import *
import Site
from Site import *
import DBConnection
from DBConnection import *
import Notifier
from Notifier import *

class Operator(object):
    '''
    Performs all necessary actions by calling functions
    '''
    

    def __init__(self, args, conf):
        '''
        Constructor
        '''
        
        self.newEntryCount = 0
        self.log = Logger(args, conf)
        self.site = Site(args, conf)
        self.db = DBConnection(args, conf)
        self.notifier = Notifier(args, conf)
    
    def act(self):
        self.log.write("Start")
        self.site.openSite()
        headers = self.site.findAllIDsOfName("jobApplication")
        
        if (len(headers) == 0):
            return
        
        jobs = self.site.findAllClassesOfName("jobTitle")
        
        if (len(jobs)):
            return
        
        for job in jobs:
            if (self.db.findJobEntry(job)):
                continue
            
            self.db.saveJobEntry(job)
            self.newEntryCount += 1
            self.log.write("Found and Saved new Job")
        
        self.notify()
    
    def notify(self):
        if (not self.notifier.notify()):
            self.log.write("Error: Cannot notify by email.")

