# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:57:41 2022

@author: Ignacio
"""


# import sqlite3
from sqlite3 import Error

from create_connection import create_connection


# def create_connection(db_file):
#     """ create a database connection to the SQLite database
#         specified by db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         return conn
#     except Error as e:
#         print(e)

#     return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_data(conn, insert_data_table, entry_list):
    """ insert data into a table from the insert_data_table statement
    :param conn: Connection object
    :param insert_data_table: a INSERT statement
    :return:
    """
    try:
        c = conn.cursor()
        c.executemany(insert_data_table, entry_list)
        conn.commit()
    except Error as e:
        print(e)
        
def convertToBinaryData(filename):
      
    # Convert binary format to images 
    # or files data
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def main():
    database = r"D:/Programacion/GestorPeticiones/database.db"
    
    # Create Table Statements
    
    sql_create_estacion_table = """ CREATE TABLE IF NOT EXISTS Estacion (
                                        eID integer PRIMARY KEY AUTOINCREMENT,
                                        nombre text NOT NULL
                                        ); """

    sql_create_contratista_table = """CREATE TABLE IF NOT EXISTS Contratista (
                                        CIF integer PRIMARY KEY,
                                        razon text NOT NULL
                                        );"""
    
    sql_create_trabajador_table = """CREATE TABLE IF NOT EXISTS Trabajador (
                                        tID integer PRIMARY KEY AUTOINCREMENT,
                                        nombre text NOT NULL,
                                        apellidos text NOT NULL,
                                        categoria_profesional text NOT NULL,
                                        usuario text NOT NULL UNIQUE,
                                        contraseña text NOT NULL,
                                        foto BLOB,
                                        administrador text NOT NULL
                                        );"""
    
    sql_create_contrato_table = """CREATE TABLE IF NOT EXISTS Contrato (
                                        cID integer NOT NULL,
                                        eID integer NOT NULL,
                                        CIF integer NOT NULL,
                                        descripcion text NOT NULL,
                                        inicio text NOT NULL,
                                        fin text NOT NULL,
                                        importe_destinado real,
                                        remanente_destinado real,
                                        importe_total real,
                                        PRIMARY KEY(cID, eID)                                        
                                        );"""
    
    sql_create_solicitud_table = """CREATE TABLE IF NOT EXISTS Solicitud (
                                        pID integer PRIMARY KEY AUTOINCREMENT,
                                        descripcion text,
                                        importe real,
                                        CIF integer,
                                        cID integer,
                                        eID integer,
                                        fecha_solicitud text,
                                        fecha_visado text,
                                        fecha_peticion text,
                                        fecha_devengo text,
                                        fecha_autorizacion text,
                                        solicitanteID integer,
                                        peticionarioID integer,
                                        visadorID integer,
                                        devengadorID integer,
                                        autorizadorID integer
                                        );"""
    
    # Insert data statements
    
    sql_insert_estacion_data = """INSERT INTO Estacion(nombre)
                                        VALUES (?)"""
                                 
                                    
    sql_insert_contratista_data = """INSERT INTO Contratista
                                        VALUES (?,?)"""
                                    
    sql_insert_trabajador_data = """INSERT INTO Trabajador
                                        (
                                            nombre, apellidos, categoria_profesional, 
                                            usuario, contraseña, foto, administrador
                                        )
                                        VALUES (?,?,?,?,?,?,?)"""
                                    
    sql_insert_contrato_data = """INSERT INTO Contrato
                                    VALUES (?,?,?,?,?,?,?,?,?)"""
                                    
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
    # Data to be inserted
                              
    estaciones =[
                     ('Avilés',) , 
                     ('Gijón',),
                     ('Oviedo',)
                ]
    
    contratistas = [
                       ('123456789', 'QWE'),
                       ('987654321', 'CARGO') 
                   ]
    
    trabajadores = [
                       ('Juan', 'García Estrada', 'Jefe de control de gestión y administración',
                        'jgarcia', '1234', 
                        convertToBinaryData('D:/Programacion/GestorPeticiones/foto_1.png'), 'No'),
                       ('María', 'González Suarez', 'Subdirectora estaciones noroeste', 'mgonzalez', '1234', None, 'Si') 
                    ]
    
    contratos = [
                    ('0001', '0001', '123456789', 'Limpieza general estaciones Avilés, Gijón y Oviedo', '2022-01-01', '2022-12-31', '6000', '6000', '30000'),
                    ('0001', '0002', '123456789', 'Limpieza general estaciones Avilés, Gijón y Oviedo', '2022-01-01', '2022-12-31', '12000', '12000', '30000'),
                    ('0001', '0003', '123456789', 'Limpieza general estaciones Avilés, Gijón y Oviedo', '2022-01-01', '2022-12-31', '12000', '12000', '30000')
                ]
    
    solicitudes = [
                    ('Limpieza Avilés Enero', '500', '123456789', '0001', '0001', '2022-01-21', None, None, None, None, '0001', None, None, None, None ), 
                    ('Limpieza Gijón Enero', '1000', '123456789', '0001', '0002', '2022-01-21', None, None, None, None, '0001', None, None, None, None ),
                    ('Limpieza Oviedo Enero', '1000', '123456789', '0001', '0003', '2022-01-21', None, None, None, None, '0001', None, None, None, None ),
                    ('Reparacion Puerta dañada-vandalismo', '800', '987654321', None, '0003', '2022-02-05', None, None, None, None, '0001', None, None, None, None )
                ]
        
    # create a database connection
    
    conn = create_connection(database)

    # create tables
    
    if conn is not None:
        
        create_table(conn, sql_create_estacion_table)
        create_table(conn, sql_create_contratista_table)
        create_table(conn, sql_create_trabajador_table)
        create_table(conn, sql_create_contrato_table)
        create_table(conn, sql_create_solicitud_table)

        # insert data into tables
        
        insert_data(conn, sql_insert_estacion_data, estaciones)
        insert_data(conn, sql_insert_contratista_data, contratistas)
        insert_data(conn, sql_insert_trabajador_data, trabajadores)
        insert_data(conn, sql_insert_contrato_data, contratos)
        insert_data(conn, sql_insert_solicitud_data, solicitudes)
                
    else:
        print("Error! cannot create the database connection.")
        

if __name__ == '__main__':
    main()