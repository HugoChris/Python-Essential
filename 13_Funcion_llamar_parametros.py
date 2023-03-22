# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:58:58 2023

@author: Usuario
"""

def multi(num1,num2):
    print("el resultado de multiplicar ", num1, "*",num2,
          " es :", num1*num2)
    return(num1*num2)
multi(50,num2=6)
multi(num1=50,num2=6)
multi(50,87)  
resultado=multi(5,87)
opt=resultado*1.12
print(opt)