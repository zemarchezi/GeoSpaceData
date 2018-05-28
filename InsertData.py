# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
"""
Created on May  018
@author: zemarchezi
"""
from sqlalchemy import MetaData, Table, inspect
from engine import engin
from sqlalchemy.orm import sessionmaker
from ExtractData import ExtractData
import os
import pandas as pd

class InsertData(object):
    """docstring for InsertData."""
    def __init__(self, data, table_name, database):
        self.tabnam = table_name
        self.datBase = database
        self.data = data

    def insertDat(self):
        # connect to a database
        engine = engin(user='jose', passwd='dados', database=self.datBase, host='localhost')
        conn = engine.connect()
        meta = MetaData(engine)
        # create a session
        Session = sessionmaker(bind=engine)
        Session.configure(bind=engine)
        session = Session()

        inspec = inspect(engine)

        col_nam = []
        for column in inspec.get_columns(self.tabnam):
            col_nam.append(column['name'])

        print (col_nam)
        print (self.data)

        self.data.columns = col_nam

        table = Table(self.tabnam, meta, autoload=True)

        # Inser the dataframe into the database in one bulk
        tta = self.data.to_dict(orient='records')
        try:
            conn.execute(table.insert(), tta)
        except (IntegrityError) as e:
            print (e[0])
            for i in self.data.index:
                print (i)
                tta = self.data[self.data.index==i].to_dict(orient='records')
                try:
                    conn.execute(table.insert(), tta)
                except (Exception) as e:
                    print (e[0])

        # Commit the changes
        session.commit()

        # Close the session
        session.close()
