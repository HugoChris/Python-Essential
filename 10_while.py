# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 19:19:00 2023
0

@author: Usuario
"""

num_con=input("Ingrese el # al que debo contar: ")
num_con=int(num_con)
contador=1
print("antes del while")
#while(contador<=num_con):
while(True):
    print(contador)
    contador+=1
    if contador>num_con:
        break
    print("Dentro del bucle")
print("fin del programa")