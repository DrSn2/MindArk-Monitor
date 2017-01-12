# -*- coding: utf-8 -*-
'''
Created on 11 jan. 2017

@author: Fredrick
'''

from selenium import webdriver

class Site(object):
    '''
    classdocs
    '''


    def __init__(self, args, conf):
        '''
        Constructor
        '''
        
        self.url = conf["SITE"]["url"]
        self.driver = None
        self.isDebug = args.debug
        self.isVerbose = args.verbose        
    
    def openSite(self):
        if (self.isDebug or self.isVerbose):
            print("Opening:" + self.url)
            
        self.driver = webdriver.PhantomJS(executable_path="../external/phantomjs.exe")
        self.driver.set_window_size(1120, 550) # or 1280x720??
        self.driver.get(self.url)
        
        if (self.isDebug or self.isVerbose):
            print("Opened:" + self.driver.current_url)
    
    def closeSite(self):
        if (self.isDebug or self.isVerbose):
            print("Closing site...")
            
        self.driver.quit()
        
        if (self.isDebug or self.isVerbose):
            print("Closed site.")
    
    def findAllClassesOfName(self, name):
        elements = self.driver.find_elements_by_class_name(name)
        return elements
    
    def findAllIDsOfName(self, name):
        elements = [self.driver.find_element_by_id(name)]
        return elements
    
    def findByXPatth(self, string):
        elements = self.driver.find_element_by_xpath(string)
        return elements
    
    def getJobEntry(self, title):
        
        jobEntry = ['head', 'desc']
        return jobEntry