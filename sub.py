# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 23:55:11 2016

@author: lstanevich
"""

print ('inside sub.py')
print ('-'*50)
print ('importing main.py')
import python_log_test
print ('imported main.py')
import logging
print ('getting logger instance in sub')
sub_logger = python_log_test.main_logger
print ('got logger instance in sub')
sub_logger.info("utilizing sub_logger")
print ('exiting sub.py')
print ('-'*50)