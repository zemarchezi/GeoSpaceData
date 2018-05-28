# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
"""
Created on May  2018
@author: zemarchezi
"""
import numpy as np
from spacepy import pycdf
import os
import glob
import pandas as pd
#
#
##################################################################
# Functions used to Separate the desired data from
# the Van Allen probes repository.
##################################################################
#
class ExtractData():
    def __init__(self, filename, directory, flag):
        self.filen = [filename]
        self.rem = flag
        self.dir = directory

    def seeVariables(self):
        files = []
        files_rept = []
        for names in self.filen:
            local_file_rept = self.dir + names
            print (local_file_rept)
            files_rept.append(glob.glob(local_file_rept)[0])
        self.files = files_rept
        print (self.files)
        data = pycdf.CDF(self.files[0])
        print (data)


    def readData(self):
        files = []
        files_rept = []
        for names in self.filen:
            local_file_rept = names
            print (local_file_rept)
            files_rept.append(glob.glob(local_file_rept)[0])
        self.files = files_rept
        print (self.files)
        self.data = pycdf.CDF(self.files[0])

        return (self.data)

    def extractData(self, variables):
        # var_rept = variables
        self.var = variables
        print ('Variables to extract:')
        print (self.var)
        self.rep = pd.DataFrame(index=self.data[self.var[0]][...])
        for v in range(0,len(self.var)):
            print ('Extracting...')
            print (self.var[v])
            dd = (self.data[self.var[v]][...])
            if len(dd.shape) == 1 and len(dd) == len(self.data[self.var[0]][...]):
                self.rep[self.var[v]] = np.transpose(dd)
            elif len(dd.shape) < 3 and len(dd) < len(self.data[self.var[0]][...]):
                energy_v = dd
            elif len(dd.shape) == 2 and len(dd) == len(self.data[self.var[0]][...]):
                temp = []
                for i in range(0,dd.shape[1]):
                    temp.append(dd[:,i])
                en = pd.DataFrame(np.transpose(temp),index=self.data[self.var[0]][...])
                for i in range(0,len(energy_v)):
                    self.rep[energy_v[i]] = en[i]
            elif len(dd.shape) == 3 and len(dd) == len(self.data[self.var[0]][...]):
                ind = v
                temp = []
                for i in range(0,dd.shape[2]):
                    temp2 = []
                    for j in range(0,dd.shape[0]):
                        temp2.append(np.mean(dd[j,:,i]))
                    temp.append(temp2)
                en = pd.DataFrame(np.transpose(temp),index=self.data[self.var[0]][...])
                for i in range(0,len(energy_v)):
                    self.rep[energy_v[i]] = en[i]

        self.rep.where(self.rep > -999999, inplace=True)

        return (self.rep)

    # Extract single variable for .cdf file
    def cdf_singleVar(self,variable):
        data = pycdf.CDF(self.files)
        var = data[variable][...]
        return var
