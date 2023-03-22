# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:46:37 2023

@author: Usuario
"""

def fib(n):
    a,b =0,1
    while a<n:
       print(a,end=' ') # end te imprime en una misma linea
       a,b = b, a+b
    print()
#fib(8)