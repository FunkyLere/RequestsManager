# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 10:38:49 2022

@author: Ignacio
"""

import pandas as pd
from create_connection import create_connection

def query(statement):
    
    database = r"D:/Programacion/GestorPeticiones/database.db"
    
    conn = create_connection(database)    
        
    DFresult = pd.read_sql_query(statement, conn)
    
    return DFresult

print(query('SELECT * FROM Trabajador;'))

