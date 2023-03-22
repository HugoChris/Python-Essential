# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:22:49 2023

@author: Usuario
"""

def isYearLeap(year):

#

# Su codigo AQUI

#

 

testData = [1900, 2000, 2016, 1987]

testResults = [False, True, True, False]

for i in range(len(testData)):

            yr = testData[i]

            print(yr,"->",end="")

            result = isYearLeap(yr)

            if result == testResults[i]:

                        print("OK")

            else:

                        print("Failed")