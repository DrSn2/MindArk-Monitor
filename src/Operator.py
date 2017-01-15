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
        
        i = 0
        textToggles = self.site.findByRelativeXPath("//a[starts-with(@onclick,'switchMenu')]")
        for job in entries:
            if (self.isVerbose):
                print("Scraping jobinfo...")
            
            splitData = job.text.splitlines()
            
            entryData = [splitData[0], str.join("\n", splitData[1:])]  # jobEntry is defined as list, [title, description]
            
            # Fix problem with empty descriptions, by clicking the switchmenu
            if (len(entryData[1]) < 250):
                textToggles[i].click()
                desc = self.site.findByXPathRelativeTo("//div[starts-with(@id,'jobs_')]", job)
                entryData[1] = desc[i].text
            
            if (len(entryData) == 0):     
                self.log.write("Could not find entry data.")
                continue
            
            #dbData = self.db.findJobEntry(entryData)
            #if (len(dbData) > 0):
            #    if (entryData[0] == dbData[0] and entryData[1] == dbData[1]):
            #        continue
            
            dbData = self.db.findRecentJobEntry(entryData)
            if (len(dbData) > 0):
                continue
            
            self.db.saveJobEntry(entryData)
            self.newEntryCount += 1
            self.log.write("Found and Saved new Job")
            i += 1
        
        if (self.newEntryCount > 0):
            self.notify()        
        
        self.site.closeSite()
    
    def notify(self):
        """ Report back to user via email """
        if (not self.notifier.notify(self.newEntryCount)):
            self.log.write("Error: Cannot notify by email.")

