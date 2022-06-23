# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 10:38:49 2022

@author: Ignacio
"""

import pandas as pd
from create_connection import create_connection

data = r"D:/Programacion/GestorPeticiones/database.db"

def query(statement, database):
      
    conn = create_connection(database)    
        
    DFresult = pd.read_sql_query(statement, conn)
    
    return DFresult

# print(query('SELECT usuario, contraseña FROM Trabajador WHERE usuario = 'jgarcia';', data))

def queryRegistro(database):
    
    """
    Parameters
    ----------
    database : A .db SQL database

    Returns
    -------
    The data frame that is going to be used in the GUI's Registro menu 

    """
    
    conn = create_connection(database)   
    
    query = 'SELECT E.eID, E.nombre, S.fecha_solicitud, S.importe,\
                    S.descripcion, S.fecha_autorizacion, S.cID, C.razon \
            FROM Estacion E, Solicitud S, Contratista C \
            WHERE S.eID = E.eID and S.CIF = C.CIF \
            ORDER BY S.fecha_solicitud DESC;'
                                
      
    DataFrame = pd.read_sql_query(query, conn, dtype = {'cID': 'Int64'})
    
    return DataFrame

def queryDetallePAO(database, pID):
    
    """
    Parameters
    ----------
    database : A .db SQL database
    sID: The request ID to locate associate data

    Returns
    -------
    The data frame that is going to be used in the GUI's Detalle PAO menu 

    """
    
    conn = create_connection(database)   
    

                
    mainQuery = f'\
                SELECT DISTINCT S.pID, S.descripcion, E.nombre, S.cID, S.importe,\
                    sub.razon, sub.inicio, sub.fin, sub.remanente_destinado,\
                    sub.consumido_destinado, sub.importe_destinado, sub.remanente_total,\
                    sub.consumido_total, sub.importe_total,\
                   	(\
                   		SELECT nombre\
                   		FROM Trabajador, Solicitud\
                   		WHERE solicitanteID = tID\
                   	) as solicitante, fecha_solicitud,\
                   	(\
                   		SELECT nombre\
                   		FROM Trabajador, Solicitud\
                   		WHERE peticionarioID = tID\
                   	) as peticionario, fecha_peticion,\
                   	(\
                   		SELECT nombre\
                   		FROM Trabajador, Solicitud\
                   		WHERE visadorID = tID\
                   	) as visado, fecha_visado,\
                   	(\
                   		SELECT nombre\
                   		FROM Trabajador, Solicitud\
                   		WHERE devengadorID = tID\
                   	) as devengado, fecha_devengo,\
                   	(\
                   		SELECT nombre\
                   		FROM Trabajador, Solicitud\
                   		WHERE autorizadorID = tID\
                   	) as autorizado, fecha_autorizacion\
                FROM Estacion E, Solicitud S, Contratista, Contrato\
                LEFT JOIN\
            	(\
                	SELECT DISTINCT razon, inicio, fin, remanente_destinado, \
                        consumido_destinado, importe_destinado, remanente_total, \
                        (Contrato.importe_total - rem_tot.remanente_total) as consumido_total, \
                        importe_total \
                    FROM \
                    ( \
                         SELECT SUM(remanente_destinado) as remanente_total, \
                             (importe_destinado - remanente_destinado) as consumido_destinado \
                         FROM Contrato C, Solicitud S \
                         WHERE S.pID = {pID} and S.cID = C.cID \
                    ) as rem_tot,Contratista, Contrato, Solicitud S\
                	WHERE Contrato.eID = \
                	(\
                		SELECT eID\
                		FROM Solicitud\
                		WHERE pID = {pID} \
                	)\
                	and Contratista.CIF = Contrato.CIF and S.cID = Contrato.cID\
                ) Sub\
                ON S.cID = Contrato.cID \
                WHERE S.pID = {pID} and E.eID = S.eID\
                ;'
                                
    citiesQuery = f'\
                    SELECT E.nombre\
                    FROM Estacion E, Solicitud S, Contrato C\
                    WHERE S.pID = {pID} and S.cID = C.cID and C.eID = E.eID;'
                    
    DataFrame = pd.read_sql_query(mainQuery, conn)
    
    return DataFrame

# df = queryRegistro(data)
# print(type(df['cID'][1]))
# print(df)

df = queryDetallePAO(data, '0001')
# print(type(df['cID'][1]))
print(df)