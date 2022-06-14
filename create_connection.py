# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 15:34:03 2022

@author: Ignacio
"""

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    # finally:
    #     if conn:
    #         conn.close()
    return conn
            
if __name__ == '__main__':
    create_connection(r"D:\programacion\GestorPeticiones\database.db")
        