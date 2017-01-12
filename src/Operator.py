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
        
        self.isDebug = args.debug
        self.isVerbose = args.verbose
        
        self.newEntryCount = 0
        self.log = Logger(args, conf)
        self.site = Site(args, conf)
        self.db = DBConnection(args, conf)
        self.notifier = Notifier(args, conf)
    
    def act(self):
        """ The main brains of the application """
        self.log.write("Start")
        self.site.openSite()
        
        if (self.isVerbose):
            print("Finding entries...")
            
        entries = self.site.findAllClassesOfName("jobApplication")
        
        if (len(entries) == 0):
            self.site.closeSite()
            if (self.isVerbose):
                print("No entries found.")
            return
        
        if (self.isVerbose):
            print("Entries found.")
        
        for job in entries:
            if (self.isVerbose):
                print("Finding jobtitles...")
            
            splitData = job.text.splitlines()
            print(splitData[0])
            print(str.join("\n", splitData[1:]))
            
            entryData = [splitData[0], str.join("\n", splitData[1:])] #= self.db.findJobEntry(job) # jobEntry is defines as list, [title, description]
            
            if (len(entryData) == 0):     
                self.log.write("Could not find entry data.")
                continue
            
            self.db.saveJobEntry(entryData)
            self.newEntryCount += 1
            self.log.write("Found and Saved new Job")
        
        self.notify()
        self.site.closeSite()
    
    def notify(self):
        """ Report back to user via email """
        if (not self.notifier.notify(self.newEntryCount)):
            self.log.write("Error: Cannot notify by email.")

