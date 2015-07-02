# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


def TableExist(Name):

    with lite.connect('imperium.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
    return Name in tables


def TableCreate(Name, schema):
    
    with lite.connect('imperium.db') as connection:
        cursor = connection.cursor()
        
        try:
            cursor.execute("CREATE TABLE " + Name + "(" + schema + ")")
            connection.commit()
        except OperationalError: 
            None


def TableFill(Name, vals):

    with lite.connect('imperium.db') as connection:
        cursor = connection.cursor()

        cursor.executemany("INSERT INTO " + Name + 
                           " VALUES(?,?,?);", vals)
        connection.commit()
        

def TableShow(Name):

    with lite.connect('imperium.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM ' + Name + ';')
        print cursor.fetchall()


def TableDrop(Name):
    
    with lite.connect('imperiumb.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DROP TABLE ' + Name + ';')
        connection.commit()
