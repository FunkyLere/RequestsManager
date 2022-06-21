# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 13:15:09 2022

@author: LENOVO
"""

# import Request
import Profile
# import PageController
# import sys
import tkinter as tk
import pruebas
import Main_frames
import RRG
from create_connection import create_connection

# variables and function from multiples auxiliares uses


def cargarVisualizacionPagina(data_page,data_visualization_values): #Extree registro uno a uno y va cargando los datos hasta 26. Recibe los datos de la pagina a mostrar, 26 registros por pagina
    for i in range(len(data_page)):
        data_visualization_values[i]['ID_station'].set(data_page[i]['ID_station'])
        data_visualization_values[i]['Station_name'].set(data_page[i]['Station_name'])
        data_visualization_values[i]['Description'].set(data_page[i]['Description'])
        data_visualization_values[i]['Budget'].set(data_page[i]['Budget'])
        data_visualization_values[i]['Contract'].set(data_page[i]['Contract'])
        data_visualization_values[i]['Contractor'].set(data_page[i]['Contractor'])


conn = create_connection(r'C:\Users\LENOVO\Desktop\python\gestorPAOs\data base code\database.db')



root=tk.Tk()
root.geometry('1750x900')
root.title('Gestor PAOs version 1.0 220604')
root.iconbitmap('Png files\icono_adif.ico')
root.resizable(False, False)
root.configure(bg='black')

# Creo todos los frames principales para ser el soporte de cada pantalla del programa.

login_frame = Main_frames.MainFrame(root, 'login frame', 1750, 900, 'grey')
PAO_frame = Main_frames.MainFrame(root, 'PAO frame', 1750, 900, 'grey')
registers_frame = Main_frames.MainFrame(root, 'main frame', 1750, 900, 'green')
login_frame.frame.grid(row = 0, column = 0)
PAO_frame.frame.grid(row=0,column=0)
registers_frame.frame.grid(row = 0, column = 0)





#----------------
#FRAME FOR LOGIN-
#----------------
root_bg_image=tk.PhotoImage(file='Png files\Logo_Adif_sin_texto.png')
label_logo = tk.Label(login_frame.frame, width =1200, height = 900, image = root_bg_image)
label_logo.place(x = 0, y = 0)
        
        # label_solicitud_formal_name = tk.Label(frame_PAO_solicitud, text = perfil_activo.formal_name, font = ('Arial',12),bg='yellow')
        # label_solicitud_formal_name.place(x = 85, y = 17)
        # label_solicitud_category = tk.Label(frame_PAO_solicitud, text = perfil_activo.category, font = ('Arial',12),bg='yellow')
        # label_solicitud_category.place (x = 85, y = 40)

#--------------------------------------------------
#FRAME MAIN WHERE A MAJORITY OF ACTION TAKES PLACE-
#--------------------------------------------------

frame_main_data=tk.Frame(registers_frame.frame, width=1230, height=800) # en este frame se pondran 32 registros de 6 columnans.

frame_main_data.place(x=260, y=50)


height=25
x=0
y=0
for register in RRG.getRandomRegisters(frame_main_data, 32): #se van a mostrar 32 registros con 6 campos.
    register.showRegister(0,y)
    y+=height

#----------------------------------------------------------
# FRAME DE UNA PAO EN CONCRETO Y VER SU ESTADO Y EVOLUCION-
#----------------------------------------------------------




frame_main_peticion=tk.Frame(PAO_frame.frame, width=320, height=125, bg='purple')
frame_main_peticion.place(x=370, y=750)

frame_main_visado=tk.Frame(PAO_frame.frame, width=320, height=125, bg='pink')
frame_main_visado.place(x=715, y=750)

frame_main_devengo=tk.Frame(PAO_frame.frame, width=320, height=125, bg='red')
frame_main_devengo.place(x=1060, y=750)

frame_main_autorizacion=tk.Frame(PAO_frame.frame, width=320, height=125, bg='blue')
frame_main_autorizacion.place(x=1405, y=750)


































root.mainloop()