# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 21:22:05 2022

@author: LENOVO
"""
import tkinter as tk
import Main_frames

class Profile(object):
    profiles={}
    active_profile = None
    creator_profile = None
    petitioner_profile = None
    visado_profile = None
    devengo_profile = None
    autorization_profile = None
    
    
    
    @classmethod #this class method read the data for all profiles from the dataframe from de ddbb
    def readProfiles(nombre,): 
        pass
    
    @classmethod #this class method is used to create a complete new profilem not read frmm ddbb
    def createProfile():
        pass
    
    
    
    def __init__(self, nombre, apellidos, contraseña, formal_name, categoria, ID_profile, picture, privileges):
        self.tID = ID_profile
        self.nombre = nombre
        self.apellidos = apellidos
        self.contraseña = contraseña
        self.categoria = categoria
        
        self.picture = picture
        Profile.profiles[self.user_name] = self
        self.frame_PAO_solicitud = None
        
    def showProfileInFramePAO(self, master, type_profile):
        if type_profile == 'Creator profile':
            self.frame_PAO_solicitud=tk.Frame(master, width=320, height=125, bg='yellow')
            self.frame_PAO_solicitud.place(x=25, y=750)
            print(self.picture)
            picture = tk.PhotoImage(file = self.picture)
            picture_label = tk.Label (self.frame_PAO_solicitud, image = picture)
            picture_label.image = picture
            formal_name_label = tk.Label(self.frame_PAO_solicitud, text = self.formal_name)
            category_label = tk.Label(self.frame_PAO_solicitud, text = self.category)
            picture_label.place(x = 0, y = 0)
            formal_name_label.place(x = 200, y = 50)
            category_label.place (x = 200, y = 100)
            
        # elif type_profile == 'Petioner profile':
            
        # elif type_profile == 'Visado profile'
        
        # elif type_profile == 'Devengo profile'
        
        # elif type_profile == 'Autorization profile'
        
        
        
    def getIDProfile(self):
        return self.ID_profile
    
    def getUserName(self):
        return self.user_name
    
    def getPassword(self):
        return self.password
    
    def getFormalName(self):
        return self.formal_name
    
    def category(self):
        return self.category
    
    def picture(self):
        return self.picture
    
    def privileges(self):
        return self.privileges
    
prueba1=Profile('piwok1','b','catalina la grande 1','emperatriz','01','foto_1.png','p')
prueba2=Profile('piwok2','b','catalina la grande 2','emperatriz','02','foto_2.png','p')
prueba3=Profile('piwok3','b','catalina la grande 3','emperatriz','03','foto_3.png','p')
prueba4=Profile('piwok4','b','catalina la grande 4','emperatriz','04','foto_4.png','p')
prueba5=Profile('piwok5','b','catalina la grande 5','emperatriz','05','foto_5.png','p')
Profile.profiles['piwok1'] = prueba1
Profile.profiles['piwok2'] = prueba2
Profile.profiles['piwok3'] = prueba3
Profile.profiles['piwok4'] = prueba4
Profile.profiles['piwok5'] = prueba5







