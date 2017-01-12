# -*- coding: utf-8 -*-
'''
Created on 11 jan. 2017

@author: Fredrick
'''

import pymysql.cursors

class DBConnection(object):
    '''
    Handles data communication to & from MySQL database
    '''


    def __init__(self, args, conf):
        '''
        Constructor
        '''
        self.server     = conf["DATABASE"]["server"]
        self.port       = conf["DATABASE"]["port"]
        self.database   = conf["DATABASE"]["database"]
        self.username   = conf["DATABASE"]["username"]
        self.password   = conf["DATABASE"]["password"]
        
        self.connection = None
        self.cursor = None
        
    def connect(self):
        """ Connect to db """
        # Connect to the database
        self.connection = pymysql.connect(host=self.server,
                             user=self.username,
                             password=self.password,
                             db=self.database,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    
    def disconnect(self):
        """ Disconnect from db """
        self.connection.close()
    
    def query(self, sql):
        """ Execute read query """
        self.cursor = self.connection.cursor()
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        
        return result
    
    def execute(self, sql):
        """ Execute write query """
        self.cursor = self.connection.cursor()
        self.cursor.execute(sql)
        self.connection.commit()
        return 0
    
    def writeLog(self, message):
        """ Write entry into log table """
        try:
            self.connect()
            self.execute("insert into log (created, message) values (now(), '" + message + "');")
            self.disconnect()
        except Exception:
            return False
        
        return True
    
    def saveJobEntry(self, jobEntry):
        """ Write entry into jobentries table """
        try:
            self.connect()
            self.execute("insert into jobentries (found, name, description) values (now(), '" + jobEntry[0] + "', '" + jobEntry[1] + "');")
            self.disconnect()
        except Exception:
            return False
        
        return True
    
    def findJobEntry(self, jobEntry):
        """ Find job entry in DB """
        result = None
        try:
            self.connect()
            result = self.query("select name, description from jobentries where name ='" + jobEntry[0] + "';")
            self.disconnect()
        except Exception:
            return []
        
        return [result[0][0], result[0][1]]