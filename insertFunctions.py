# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 10:50:24 2022

@author: Ignacio
"""


from create_connection import create_connection
from createTable import insert_data

database = r"D:/Programacion/GestorPeticiones/database.db"
   
        
def insert_estacion(data):
    
    """
    Parameters
    ----------
    data : A list containing a tuple with the following data as strings:
        nombre

    Returns
    -------
    None. Inserts data into Estacion table

    """
     
    sql_insert_estacion_data = """INSERT INTO Estacion(nombre)
                                        VALUES (?)"""
    conn = create_connection(database)
    
    if conn is not None:
        insert_data(conn, sql_insert_estacion_data, data)
    else:
            print("Error! cannot create the database connection.")

            
def insert_contratista(data):
    
    """
    Parameters
    ----------
    data : A list containing a tuple with the following data as strings:
        cif, razon

    Returns
    -------
    None. Inserts data into trabajador table

    """
     
    sql_insert_contratista_data = """INSERT INTO Contratista
                                        VALUES (?,?)"""
    conn = create_connection(database)
    
    if conn is not None:
        insert_data(conn, sql_insert_contratista_data, data)
    else:
        print("Error! cannot create the database connection.")
            
                        
def insert_trabajador(data):
    
    """
    Parameters
    ----------
    data : A list containing a tuple with the followingdata as strings:
        nombre, apellidos, categoria_profesional, usuario, contraseña, foto, administrador

    Returns
    -------
    None. Inserts data into trabajador table

    """
     
    sql_insert_trabajador_data = """INSERT INTO Trabajador
                                        (
                                            nombre, apellidos, categoria_profesional, 
                                            usuario, contraseña, foto, administrador
                                        )
                                        VALUES (?,?,?,?,?,?,?)"""
    conn = create_connection(database)
    
    if conn is not None:
        insert_data(conn, sql_insert_trabajador_data, data)
    else:
        print("Error! cannot create the database connection.")
               
            
def insert_contrato(data):
    
    """
    Parameters
    ----------
    data : A list containing a tuple with the followingdata as strings:
        cID, eID, cif, descripcion, inicio, fin, importe_destinado, remanente_destinado, importe_total

    Returns
    -------
    None. Inserts data into contrato table

    """
    
    sql_insert_contrato_data = """INSERT INTO Contrato
                                VALUES (?,?,?,?,?,?,?,?,?)"""
    conn = create_connection(database)
    
    if conn is not None:
        insert_data(conn, sql_insert_contrato_data, data)
    else:
        print("Error! cannot create the database connection.")
    
    
def insert_solicitud(data):
     
    """
    Parameters
    ----------
    data : A list containing a tuple with the following data as strings:
        descripcion, importe, cif, cID, eID, fecha_solicitud, fecha_visado, fecha_peticion, fecha_devengo, fecha_autorizacion, solicitanteID, peticionarioID, visadorID, devengadorID, autorizadorID

    Returns
    -------
    None. Inserts data into solicitud table

    """
    
    sql_insert_solicitud_data = """INSERT INTO Solicitud
                                    (
                                        descripcion, importe, CIF, cID, eID,
                                        fecha_solicitud, fecha_visado,
                                        fecha_peticion, fecha_devengo,
                                        fecha_autorizacion, solicitanteID,
                                        peticionarioID, visadorID, devengadorID,
                                        autorizadorID
                                    )
                                    VALUES
                                    (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""                             
    conn = create_connection(database)
    
    if conn is not None:
        insert_data(conn, sql_insert_solicitud_data, data)
    else:
        print("Error! cannot create the database connection.")
    

    