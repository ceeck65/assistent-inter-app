# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 00:18:06 2023

@author: alesp
"""

import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


# import sqlite3



def createConnection():
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName("modules/Databases/database.db")
    if not connection.open():
        print("Database Error: %s" % connection.lastError().databaseText())
        return False
    return True


def getQuery(sql):
     query = QSqlQuery(sql)
     return query
     


if not createConnection():
    sys.exit(1)
else:
    print("Connection successfull")


