#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 09:46:00 2018

@author: jose
"""

from sqlalchemy import create_engine, MetaData, Table, inspect
import sqlalchemy as sqla
from base import Base
from engine import engin
from sqlalchemy.orm import sessionmaker, relationship
from ExtractData import ExtractData
import datetime
import os

probe = 'A'
path = os.getcwd() #'/home/jose/MEGA/Doutorado/Progs/plot_ULF/dados/'
dataDownlDir = '/home/jose/Documents/dados/data_rept'+probe.lower()+'/' #path + '/data/'
dataOmniDownlDir = dataDownlDir + '/omni/'
plotDir = dataDownlDir + '/plots/' # path + '/plots/'


ee = ExtractData(filename='*20140912*', variables=['Epoch', 'L', 'L_star', 'FEDU_Energy', 'FEDU', 'MLT'], directory=dataDownlDir, flag=0)

rep = ee.extract_rept()

energy_values = []
for i in range(0,12):
    energy_values.append('en_lev_'+str(i+1))

bb = []
bb.append(rep[0][0])
for s in rep[4][0]:
    bb.append(s)








engine = engin(user='jose', passwd='dados', database='VanAllenA', host='localhost')

meta = MetaData(engine)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()


tes = Rept(id=datetime.datetime(2015,6,4), lshell=1,lstar=1.5, mlt=2.65, en_lev_1=9.5,en_lev_2=9.5,en_lev_3=9.5, en_lev_4=9.5, en_lev_5=9.5, en_lev_6=9.5, en_lev_7=9.5, en_lev_8=9.5, en_lev_9=9.5, en_lev_10=9.5, en_lev_11=9.5, en_lev_12=9.5)

for table_name in inspector.get_table_names():
    print ("Name: %s" % table_name)
    for column in inspector.get_columns(table_name):
        print("Column: %s" % column['name'])
