#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 11 jan. 2017

@author: Fredrick
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Notifier(object):
    '''
    Sends email notifications.
    '''


    def __init__(self, args, conf):
        '''
        Constructor
        '''
        self.server     = conf["EMAIL"]["server"]
        self.port       = int(conf["EMAIL"]["port"])
        self.username   = conf["EMAIL"]["username"]
        self.password   = conf["EMAIL"]["password"]
        self.sender     = conf["EMAIL"]["sender"]
        self.recipient  = conf["EMAIL"]["recipient"]
        
        self.siteURL = conf["SITE"]["url"]
        
        self.args = args
    
    def notify(self):
        """ Send report email """
        try:
            if (self.args.debug or self.args.verbose):
                print("Constructing email...")
            msg = MIMEMultipart()
            msg['From'] = self.sender
            msg['To'] = self.recipient
            msg['Subject'] = "MindArk Monitoring System"
             
            body = """A new position at MindArk was found!
            Hurry, go there an take a look.""" + self.siteURL
            
            msg.attach(MIMEText(body, 'plain'))
            if (self.args.debug or self.args.verbose):
                print("Email constructed.")
            
            if (self.args.debug or self.args.verbose):
                print("Signing in...")
            server = smtplib.SMTP(self.server, self.port)
            server.starttls()
            server.login(self.username, self.password)
            if (self.args.debug or self.args.verbose):
                print("Signed in.")
            
            if (self.args.debug or self.args.verbose):
                print("Sending email.")
            text = msg.as_string()
            server.sendmail(self.sender, self.recipient, text)
            server.quit()
            if (self.args.debug or self.args.verbose):
                print("Email sent.")
        except Exception:
            return False
        
        return True