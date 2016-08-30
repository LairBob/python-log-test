# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 20:30:20 2016

@author: lstanevich
"""

import logging

def main():
    print("Testing")
    logger = logging.getLogger()
    fhandler = logging.FileHandler(filename='log_test.log', mode='w')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fhandler.setFormatter(formatter)
    logger.addHandler(fhandler)
    logger.setLevel(logging.DEBUG)
     
    try:
        raise RuntimeError
    except Exception:
        logger.exception("Error!")

if __name__ == "__main__":
    main()