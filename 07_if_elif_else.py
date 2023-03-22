# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:31:09 2023

@author: Usuario
"""

acl=int(input("ingrese el # de ACL: "))
if acl >=1 and acl<=99:
    print("Laa ACL es estandar")
elif acl >=100 and acl<=199:
    print("Laa ACL es extendida")
else:
    print("Laa ACL es extendida")
    
