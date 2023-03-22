# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:43:06 2023

@author: Usuario
"""

age = int(input("Ingrese su edad:  "))
space = ""
if age >=1 and age<=10:
    print("Es Nino")
elif age >=10 and age<=15:
    print("Es adolecente")
elif age >=16 and age<=25:
     print("Es joven")
else:
    print("Adulto")
