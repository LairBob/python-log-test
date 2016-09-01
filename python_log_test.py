# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 20:30:20 2016

@author: lstanevich
"""

import logging

def logger():

      print ('initializing logger....')
      logPath = '.'
      fileName = 'log_test'

      # configure log formatter
      logFormatter = logging.Formatter("%(asctime)s [%(filename)s] [%(funcName)s] [%(levelname)s] [%(lineno)d] %(message)s")

      # configure file handler
      fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName), mode="w")
      fileHandler.setFormatter(logFormatter)

      # configure stream handler
      consoleHandler = logging.StreamHandler()
      consoleHandler.setFormatter(logFormatter)

      # get the logger instance
      logger = logging.getLogger(__name__)

      # set the logging level
      logger.setLevel(logging.DEBUG)

      print ('adding handlers- ')

      #if not len(logger.handlers):
      logger.addHandler(fileHandler)
      logger.addHandler(consoleHandler)

      print ('logger initialized....\n')
      print ('associated handlers - ', len(logger.handlers))
      for handler in logger.handlers:
            print (handler)
      print()
      return logger

print ('inside main.py')
print ('-'*50)

main_logger = logger()
main_logger.info('utilizing main.py logger.')
print ('exiting main.py')   
print ('-'*50)

#if __name__ == "__main__":
#    main()