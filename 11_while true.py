# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 19:46:59 2023

@author: Usuario
"""

while True:
    x=input("enter a number to cout to: ")
    if x=='q'or x=='quit':
        break
    x=int(x) #este código no funcionaba, el bloque no esta anidado correctamente
    y=1
    print("fuera del while ")
    while True:
        print(y)
        y=y+1
        if y>x:
           break
       

   