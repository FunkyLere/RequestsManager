# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 00:52:07 2022

@author: LENOVO
"""

import tkinter as tk

class PageController(object):
    
    def pageControl():
        pass
    
    
    def __init__(self, master):
        
        self.frame = tk.Frame(master, width = 360, height = 30, bg='grey')
        
        self.current_page = 1
        self.boton_anterior=tk.Button(self.frame, text = 'anterior', command = lambda: self.pageControl(self.current_page-1))
        self.boton_anterior.place(x = 0, y = 0, width = 60, height = 30)
        self.boton_1=tk.Button(self.frame, text = '1', command = lambda: self.pageControl(1))
        self.boton_1.place(x = 75, y = 0, width = 30, height = 30)
        self.boton_2=tk.Button(self.frame, text = '2', command = lambda: self.pageControl(2))
        self.boton_2.place(x = 120, y = 0, width = 30, height = 30)
        self.boton_3=tk.Button(self.frame, text = '3', command = lambda: self.pageControl(3))
        self.boton_3.place(x = 165, y = 0, width = 30, height = 30)
        self.boton_4=tk.Button(self.frame, text = '4', command = lambda: self.pageControl(4))
        self.boton_4.place(x = 210, y = 0, width = 30, height = 30)
        self.boton_5=tk.Button(self.frame, text = '5', command = lambda: self.pageControl(5))
        self.boton_5.place(x = 255, y = 0, width = 30, height = 30)

        self.boton_siguiente=tk.Button(self.frame, text = 'siguiente', command = lambda: self.pageControl(self.current_page+1))
        self.boton_siguiente.place(x = 300, y = 0, width = 60, height = 30)
        
    def showPageController(self, x, y):
        self.frame.place(x = x, y = y)

# root=tk.Tk()

# prueba = PageController(root)
# prueba.showPageController(20,20)





# root.mainloop()
        