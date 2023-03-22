# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:56:32 2023

@author: Usuario
"""
lista2=[]
lista=["R1","R2","R3","S1","S2","S3"]
print(len(lista))
#print(lista[0])

for item in lista:
  #  print(item)
  if  "R" in item:   #va a imprir los items con contengan la letra R
  lista2.append(item)  
  
  #print(item,end  *  ")