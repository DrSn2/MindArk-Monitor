#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 10 jan. 2017

@author: Fredrick
'''

import argparse     # Parsing arguments
import configparser # Parse .ini-files

import Operator
from Operator import *

# Globals
args = None # Execution arguments
conf = None # Config data
operator = None # Application Operator

def getArgParser():
    """ Prepares argument parser """
    parser = argparse.ArgumentParser("Keeps an eye on the MindArk Career site, notifying on changes.")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")
    
    parser.add_argument("-V", "--verbose", action="store_true", help="Print out what detailed event information to stdout.")
    parser.add_argument("-q", "--quiet", action="store_true", help="Print nothing to stdout.")
    parser.add_argument("-d", "--debug", action="store_true", help="Debug behaviour")
    parser.add_argument("-c", "--config-file", help="Config-file filename.")
    
    return parser

def getArgs():
    """ Fetches the command-line arguments """
    global args
    parser = getArgParser()
    args = parser.parse_args()

def dumpArgs():
    """ Dumps all args to std out """
    print("== ARGS ==")
    #print(args.version)
    #print(args.verbose)
    #print(args.quiet)
    print("Debug:", args.debug)
    #print(args.config-file)

def readConfig(filename):
    """ Returns the config content as a dict och dicts """
    global conf
    conf = configparser.ConfigParser()
    conf.read(filename, encoding='UTF-8')

def dumpConfig():
    """ Dumps all config info to std out """
    global conf
    print("== CONFIG ==")
    print("DEFAULT")
    for key in conf["DEFAULT"]:
            value = conf["DEFAULT"][key]
            print("\t" + key +"="+ value)
    
    for dic in conf.sections():
        print(dic)
        for key in conf[dic]:
            value = conf[dic][key]
            print("\t" + key +"="+ value)

def init():
    """ Initializes application """
    global args
    getArgs()
    if (args.debug):
        dumpArgs()

    confFileName = "./mamon.conf"
    if (args.config_file):
        confFileName = args.config_file
    readConfig(confFileName)
    if (args.debug):
        dumpConfig()
    
    global conf
    global operator
    operator = Operator(args, conf)

def performProcess():
    """ Calls necessary functions """
    global args
    global conf
    
    global operator
    operator.act()

def clean():
    """ Releases resources """
    pass

if __name__ == '__main__':
    """ Main function """
    init()
    performProcess()
    clean()
    
    