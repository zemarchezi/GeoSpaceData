#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 10:08:05 2018

@author: jose
"""

from sqlalchemy import create_engine

def engin(user='', passwd='', database='', host=''):
    # Connect to the database
    st = 'postgresql://'+user+':'+passwd+'@'+host+':5432/'+database
    engine = create_engine(st)
    
    return engine

