# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 00:18:06 2023

@author: alesp
"""

import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel


class Database():
    def __init__(self):
        super(Database, self).__init__()
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("modules/Databases/database.db")

               
    def createConnection(self):
        print("createConnection")
        print(self.db)
        if not self.db.open():
            print("Database Error: %s" % self.db.lastError().databaseText())
            return False 

    def getQuery(self, sql):
        self.createConnection()
        query = QSqlQuery(self.db)
        query.prepare(sql)
        query.exec()
        self.model = QSqlQueryModel()
        self.model.setQuery(query)
        return self.model

    def getSingleQuery(self, sql):
        self.createConnection()
        self.model = QSqlQueryModel()
        self.model.setQuery(sql)
        return self.model
        

    def createQuery(self, sql, args):
        self.createConnection()
        query = QSqlQuery(self.db)
        query.prepare(sql)
        for arg in args:
            query.addBindValue(arg)
        exec = query.exec()
        last_id = self.getQuery("select max(id) from templates;")
        last_id =  last_id.record(0).value(0)
        return [exec, last_id]
    

        
        