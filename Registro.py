# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 21:37:46 2022

@author: LENOVO
"""
import tkinter as tk
import Main_frames
import Profile

class Register(object):
    
    active_register= None
    #ancho total de 1230
    columns_width = {'Station ID': 40,
                    'Station name': 155,
                    'Description': 620,
                    'Budget': 80,
                    'Contract':25,
                    'Contractor': 310}
    row_height = 25
        
    def getRegisterClick(self,event):
        for label in self.labels:
            self.labels[label].configure(bg='gold')
        
    def getRegisterDoubleClick(self,event):
        Register.active_register = self
        print(self.static_vars['Creator profile'])
        print(self.static_vars['Petioner profile'])
        print(self.static_vars['Visado profile'])
        print(self.static_vars['Devengo profile'])
        print(self.static_vars['Autorization profile'])
        #---------------------------------------------------
        #visualizacion creator profile en frame detalle PAO-
        #---------------------------------------------------

        
        Profile.Profile.profiles[self.static_vars['Creator profile']].showProfileInFramePAO(Main_frames.MainFrame.main_frames['PAO frame'].frame,'Creator profile')
        
        Main_frames.MainFrame.main_frames['PAO frame'].frame.tkraise()
        

        
        
    def showRegister(self, x, y):
        x, y = x, y
        for label in self.labels:
            self.labels[label].place(x = x, y = y, width = Register.columns_width[label], height = Register.row_height)
            x+=Register.columns_width[label]
        
    def __init__(self,master, station_ID, station_name, description, budget, contract, contractor,
                 creator_profile, creation_date, petioner_profile, petition_date, visado_profile, visado_date,
                 devengo_profile, devengo_date, autorization_profile, autorization_date):
        #variables control de cambios de ventana
        self.master = master
        
        #Variables a actualizar con los valores para mostralos por pantalla
        self.dinamic_vars = {'Station ID': tk.StringVar(value = station_ID),
                             'Station name': tk.StringVar(value = station_name),
                             'Description': tk.StringVar(value = description),
                             'Budget': tk.IntVar(value = budget),
                             'Contract': tk.BooleanVar(value=contract),
                             'Contractor': tk.StringVar(value=contractor)}
        #variables de objetos Label que son los que dan la forma grafica y los datos estan vinculado a self.dinamic_vars
        self.labels = {'Station ID': tk.Label(self.master, textvariable = self.dinamic_vars['Station ID'], bg = 'grey', relief = 'ridge', border =2, anchor = 'w'),
                       'Station name': tk.Label(self.master, textvariable = self.dinamic_vars['Station name'], bg = 'grey', relief = 'ridge', border = 2, anchor = 'w'),
                       'Description': tk.Label(self.master, textvariable = self.dinamic_vars['Description'], bg = 'grey', relief = 'ridge', border = 2, anchor ='w'),
                       'Budget': tk.Label(self.master, textvariable = self.dinamic_vars['Budget'], bg = 'grey', relief = 'ridge', border = 2, anchor = 'w'),
                       'Contract': tk.Label(self.master, textvariable = self.dinamic_vars['Contract'], bg = 'grey', relief = 'ridge', border = 2, anchor = 'w'),
                       'Contractor': tk.Label(self.master, textvariable = self.dinamic_vars['Contractor'], bg = 'grey', relief = 'ridge', border = 2, anchor = 'w')}
        for label in self.labels:
            self.labels[label].bind('<Button-1>', self.getRegisterClick)
            self.labels[label].bind('<Double-Button-1>', self.getRegisterDoubleClick)
        #variables que no se muestran en la lista de registro y se usan para el detalle del registro: todos los intervinientes y la fecha de la accion
        self.static_vars = {'Creator profile': creator_profile, 'Creation date': creation_date, 'Petioner profile': petioner_profile, 'Petition date': petition_date,
                            'Visado profile': visado_profile, 'Visado date': visado_date, 'Devengo profile': devengo_profile, 'Devengo date': devengo_date,
                            'Autorization profile': autorization_profile, 'Autorization date': autorization_date}










# root=tk.Tk()
# root.geometry('1750x900')
# prueba1 = Register(root, '01','Oviedo', 'esto es una prueba', 900, True, 'Estrada', 'Profile1', 'Creation date1', 'Profile2', 'Petition date2', 'Profile3', 'Visado date3', 'Profile4', 'Devengo date4', 'Profile5', 'Autorization date5')
# prueba1.showRegister(50,50)
# prueba2 = Register(root, '02','Gijon', 'esto es otra prueba', 1250, False, 'SICE', 'Profile5', 'Creation date5', 'Profile4', 'Petition date4', 'Profile3', 'Visado date3', 'Profile2', 'Devengo date2', 'Profile1', 'Autorization date1')
# prueba2.showRegister(50,75)
# root.mainloop()

