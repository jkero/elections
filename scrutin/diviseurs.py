# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 17:09:51 2019

@author: jk
"""

def diviseurs(pop):
    resu = []
    for i in range(2,20):
        c = pop/i
        for j in range(2,50000):
           # print(c)
            if c == j:               
              resu.append(c)
              print(str(c)+ " == " + str(j))
               
    resu.sort()
    print (resu)
    
diviseurs(67890)