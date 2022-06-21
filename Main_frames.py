# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 21:17:19 2022

@author: LENOVO
"""

import tkinter as tk


class MainFrame (object):
    main_frames = {}
    
    def __init__(self, master,name, width, height, bg):
        self.master = master
        self.name = name
        self.width = width
        self.height = height
        self.bg = bg
        self.frame = tk.Frame(master, width = self.width, height = self.height, bg = self.bg)
        self.frame.grid(row = 0, column = 0)
        MainFrame.main_frames[self.name] = self