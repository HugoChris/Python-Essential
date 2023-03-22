# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:35:15 2023

@author: Usuario
"""

def saludo(nombre, apellido):
    print("Hola" , nombre, apellido, "\n")
    
saludo("Hugo","Fiallos")
saludo("Ana", "Aguilar")
saludo(input("nombre"), input("apellido"))