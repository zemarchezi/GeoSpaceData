#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 15:13:09 2018

@author: jose
"""

from sqlalchemy import Column
import sqlalchemy as sqla
from base import Base
from engine import engin
from sqlalchemy.orm import sessionmaker

class Rept(Base):
    __tablename__ = 'rept_en'

    id = Column(sqla.TIMESTAMP(timezone=False), primary_key=True)
    lshell = Column('lshell', sqla.REAL)
    lstar = Column('lstar', sqla.REAL)
    mlt = Column('mlt', sqla.REAL)
    en_lev_1 = Column('en_lev_1', sqla.REAL)
    en_lev_2 = Column('en_lev_2', sqla.REAL)
    en_lev_3 = Column('en_lev_3', sqla.REAL)
    en_lev_4 = Column('en_lev_4', sqla.REAL)
    en_lev_5 = Column('en_lev_5', sqla.REAL)
    en_lev_6 = Column('en_lev_6', sqla.REAL)
    en_lev_7 = Column('en_lev_7', sqla.REAL)
    en_lev_8 = Column('en_lev_8', sqla.REAL)
    en_lev_9 = Column('en_lev_9', sqla.REAL)
    en_lev_10 = Column('en_lev_10', sqla.REAL)
    en_lev_11 = Column('en_lev_11', sqla.REAL)
    en_lev_12 = Column('en_lev_12', sqla.REAL)


class Efw_norm(Base):
    __tablename__ = 'efw_field'

    id = Column(sqla.TIMESTAMP(timezone=False), primary_key=True)
    efield_mgsex = Column('efield_mgseX', sqla.REAL)
    efield_mgsey = Column('efield_mgseY', sqla.REAL)
    efield_mgsez = Column('efield_mgseZ', sqla.REAL)
#    spinAxis_gse = Column('spinAxis_gse', sqla.REAL)

class Efw_High(Base):
    __tablename__ = 'efwhigh_field'

    id = Column(sqla.TIMESTAMP(timezone=False), primary_key=True)
    efield_mgsex = Column('efield_mgseX', sqla.REAL)
    efield_mgsey = Column('efield_mgseY', sqla.REAL)
    efield_mgsez = Column('efield_mgseZ', sqla.REAL)


class Emfisis(Base):
    __tablename__ = 'emfisis_field'

    id = Column(sqla.TIMESTAMP(timezone=False), primary_key=True)
    magx = Column('Bx_GSE', sqla.REAL)
    magy = Column('By_GSE', sqla.REAL)
    magz = Column('Bz_GSE', sqla.REAL)
    coordinatesx = Column('x_GSE', sqla.REAL)
    coordinatesy = Column('y_GSE', sqla.REAL)
    coordinatesz = Column('z_GSE', sqla.REAL)


if __name__ == '__main__':
    # Connect to the database
    engine = engin(user='jose', passwd='dados', host='localhost', database='VanAllenA')
    # commit changes in connectDatabase
    Base.metadata.create_all(engine)
