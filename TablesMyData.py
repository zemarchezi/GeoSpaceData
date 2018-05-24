# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
"""
Created on Wed May  2 10:26:25 2018

@author: jose
"""
import numpy as np
import psycopg2
import datetime
import glob
from extractDataFunc import extract_rept, cdf_singleVar
from analysisFunc import fill_nan, replace_at_index1
import os, re, ssl, urllib, sys, fnmatch
from dataDownloader import DataDownloader
import os, fnmatch, sys


class TablesMyData():
    def __init__(self, hostname, database, user, password):
        # Parametros
        self.host = hostname
        self.database = database
        self.user = user
        self.passwd = password
        self.con = None
        self.cur = None

    def connectDatabase(self):
        try:
            # Connect to an existing database for Van allen A
            self.con = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.passwd)
            # Open a cursor to perform database operations
            self.cur = self.con.cursor()
        except Exception as e:
            print(e)


    def createTable(self, tableName):
        self.table = tableName
        ex = """CREATE TABLE public."%s" (id timestamp(2) without time zone NOT NULL, CONSTRAINT "%s_pkey" PRIMARY KEY (id)) WITH (OIDS=FALSE);
        ALTER TABLE public."%s"
            OWNER TO %s;""" %(self.table, self.table, self.table, self.user)
        try:
            self.cur.execute(ex)
            self.con.commit()
        except Exception, e:
            print e.pgerror
            self.con.rollback()

    def insertColumns(self, columns, kind):
        self.col = columns
        for i in self.col:
            ex = 'ALTER TABLE ' + self.table + ' ADD COLUMN ' + str(i) + ' ' + kind + ' NOT NULL'
            try:
                self.cur.execute(ex)
                self.con.commit()
            except Exception, e:
                print e.pgerror
                self.con.rollback()

    def insertData(self, data, tableName):
        self.dat = data
        self.table = tableName
        ex = """INSERT INTO """ +  self.table +  """ VALUES ("""
        aa = ['%s', ',']*len(self.dat)
        for i in aa[:-1]:
            ex =  ex + i
        ex = ex + """);"""
        try:
            self.cur.execute(ex, self.dat)
            self.con.commit()
        except Exception, e:
            print e.pgerror
            self.con.rollback()


    # cur.execute("""INSERT INTO public."rept_param" (id, "LShell", "LStar", "MLT") VALUES (%s,%s,%s,%s);""",(rep[0][i],rep[1][i],rep[2][i],rep[5][i]))
