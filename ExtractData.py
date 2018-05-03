#!/usr/bin/python2
# coding=utf-8
# author: zemarchezi
# read rept files
import numpy as np
from spacepy import pycdf
import os
import glob
#
#
##################################################################
# Functions used to Separate the desired data from
# the Van Allen probes repository.
##################################################################
#
class ExtractData():
    def __init__(self, filename, directory, variables, flag):
        self.filen = [filename]
        self.var = variables
        self.rem = flag
        self.dir = directory

    def extract_rept(self):
        # var_rept = variables
        files = []
        files_rept = []
        for names in self.filen:
            local_file_rept = self.dir + names
            print local_file_rept
            files_rept.append(glob.glob(local_file_rept)[0])
        self.files = files_rept
        print (self.files)

        rep = []
        for v in self.var:
            rep.append([])
            for l in self.files:
                print ('this is' , l)
                data_rept = pycdf.CDF(l)
                rep[len(rep)-1].extend(data_rept[v][...])

        for r in rep[4]:
            r[r == -9999999999999999635896294965248.000] = 'NaN'

        for i in range(0,len(rep[4])):
            temp = rep[4][i]
            temp2 = []
            for l in range(temp.shape[1]):
                temp2.append(np.nanmean(temp[:,l]))
            rep[4][i] = temp2
        if self.rem:
            for l in self.files:
                os.remove(l)
        return rep


    # Extract the variables of interest from emfsis .cdf file
    def extract_emfisis(self):
        files = []
        files_rept = []
        for names in self.filen:
            local_file_rept = self.dir + names
            print local_file_rept
            files_rept.append(glob.glob(local_file_rept)[0])
        self.files = files_rept
        print (self.files)

        emf = []
        for v in self.var:
            emf.append([])
            for l in self.files:
                data_mag = pycdf.CDF(l)
                emf[len(emf)-1].extend(data_mag[v][...])

        for i in range(1,len(emf)):
            temp = np.asmatrix(emf[i])
            temp[temp == -99999.898] = 'NaN'
            emf[i] = temp
        if self.rem:
            for l in self.files:
                os.remove(l)

        return emf

    # Extract the variables of interest from efw .cdf file
    def extract_efw(self):
        files = []
        files_rept = []
        for names in self.filen:
            local_file_rept = self.dir + names
            print local_file_rept
            files_rept.append(glob.glob(local_file_rept)[0])
        self.files = files_rept
        print (self.files)

        efw = []
        for v in self.var:
            efw.append([])
            for l in self.files:
                data_ele = pycdf.CDF(l)
                efw[len(efw)-1].extend(data_ele[v][...])

        for i in range(1,len(efw)):
            temp = np.asmatrix(efw[i])
            temp[temp == -9999999848243207295109594873856.000] = 'NaN'
            efw[i] = temp
        if self.rem:
            for l in self.files:
                os.remove(l)
        return efw

    # Extract single variable for .cdf file
    def cdf_singleVar(self,variable):
        data = pycdf.CDF(self.files)
        var = data[variable][...]
        return var
    # ##
    # #
    # Kp Download
    # def down_kp(timeini, timeend, downloadData, filename = 'none'):
    #     potsdam = downloadData # if 1, download the kp data from potsdam, if 0 you must import manually from spidr
    #     timeini = timeini
    #     timeend = timeend
    #
    #     # the filename is used only when the data is from SPIDR repository
    #     ###
    #
    #     # directory of the data
    #     path = os.getcwd() #'/home/jose/MEGA/Doutorado/Progs/plot_ULF/dados/'
    #     dataDownlDir = path + '/dados/'
    #     plotDir = path + '/plots/'
    #
    #
    #     if downloadData == 1:
    #         # Download data
    #         str_temp = 'kp%s%02d.tab' % (str(timeini.year)[2:], timeini.month)
    #         # define the directory and host in the ftp
    #         host = 'ftp.gfz-potsdam.de'
    #         working_directory = '/pub/home/obs/kp-ap/tab/'
    #         #### download of the data #################
    #         mx = MarxeDownloader(host)
    #         # Connecting
    #         mx.connect()
    #         # Set downloaded data directory
    #         mx.set_output_directory(dataDownlDir)
    #         # Set FTP directory to download
    #         mx.set_directory(working_directory)
    #         # Download single data
    #         mx.download_one_data(str_temp)
    #
    #         f = open(dataDownlDir + str_temp, 'r')
    #         data = f.readlines()
    #         f.close()
    #         data = data[:-4]
    #         useKp = data[(timeini.day-1):(timeend.day)]
    #         usekp2 = []
    #         for i in range(0, len(useKp)):
    #             temp = useKp[i].split('  ')
    #             usekp2.append([])
    #             usekp2[i].extend(temp[1].split(' '))
    #             usekp2[i].extend(temp[2].split(' '))
    #             totKpDays = []
    #         for ii in usekp2:
    #             totKpDays.extend(ii)
    #         for i in range(0, len(totKpDays)):
    #             temp = totKpDays[i]
    #             if temp[1] == 'o':
    #                 totKpDays[i] = float(totKpDays[i][0])
    #             if temp[1] == '-':
    #                 totKpDays[i] = float(totKpDays[i][0]) - 1./3
    #             if temp[1] == '+':
    #                 totKpDays[i] = float(totKpDays[i][0]) + 1./3
    #     else:
    #         kpFilename = filename
    #         kp = np.loadtxt(dataDownlDir+kpFilename,delimiter=' ', skiprows=16, usecols=(2,2), unpack=True)
    #         totKpDays = kp[0]
    #
    #     kp = totKpDays
    #     mkp = []
    #     # invert the signal of kp in order to plot togheter with the dll
    #     for i in totKpDays:
    #         mkp.append(i*-1)
    #
    #     ttt = np.linspace(1,4,len(kp))
    #
    #     # create a date array
    #     ran = (len(kp) / 8) * 24
    #     date_list2 = [datetime.datetime(timeini.year, timeini.month, timeini.day, 0, 0) + datetime.timedelta(hours=x) for x in range(0,ran,3)]
    #
    #     return (date_list2, kp, mkp)
