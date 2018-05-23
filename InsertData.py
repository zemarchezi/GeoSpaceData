#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: jose
"""
from sqlalchemy import MetaData, Table, inspect
from engine import engin
from sqlalchemy.orm import sessionmaker
from ExtractData import ExtractData
import os
import pandas as pd
import matplotlib.pyplot as plt

probe = 'A'
path = os.getcwd() #'/home/jose/MEGA/Doutorado/Progs/plot_ULF/dados/'
dataDownlDir = '/home/jose/Documents/dados/data_rept'+probe.lower()+'/' #path + '/data/'
dataOmniDownlDir = dataDownlDir + '/omni/'
plotDir = dataDownlDir + '/plots/' # path + '/plots/'


ee = ExtractData(filename='*20140914*', directory=dataDownlDir, flag=0)

ddata = ee.readData()

rep = ee.extract_rept(variables=['Epoch', 'L', 'L_star', 'FEDU_Energy', 'FEDU', 'MLT'])

# connect to a database
engine = engin(user='jose', passwd='dados', database='VanAllenA', host='localhost')
conn = engine.connect()
meta = MetaData(engine)
# create a session
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

inspec = inspect(engine)

tab_nam = 'rept_en'

col_nam = []
for column in inspec.get_columns(tab_nam):
    col_nam.append(column['name'])

rep.columns = col_nam

tta = rep.to_dict(orient='records')

table = Table(tab_nam, meta, autoload=True)

# Inser the dataframe into the database in one bulk
try:
    conn.execute(table.insert(), tta)
except Exception, e:
    print e

# Commit the changes
session.commit()

# Close the session
session.close()

for table_name in inspec.get_table_names():
    print ("Name: %s" % table_name)
    for column in inspec.get_columns(table_name):
        print("Column: %s" % column['name'])
