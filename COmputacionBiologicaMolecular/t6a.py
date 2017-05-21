#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
#PRACTICA 06-A:
""" Implemente un programa que responda:
a) Calcule la probabilidad de que haya 2C, 3G, 2A y 1T.
b) Calcule la probabilidad de que haya 2C, 3G, 2A y 1T."""
nucl={'A':'Adenina','T':'Timina', 'C': 'Citosina','G':'Guanina'}
purinas=['A','G']
pirimidina=['C','T','U']
def fact(n):
    return math.factorial(n)
def prob(abc,char):
      """Probabilidad de char en abc"""
      return float(abc.count(char))/float(len(abc))

def valeatn(a,b,c,d,pa,pb,pc,pd):
    aa=pow(pa,a)*pow(pb,b)*pow(pc,c)*pow(pd,d)
    bb=fact(8)*1.0/(fact(a)*fact(b)*fact(c)*fact(d))

    return aa*bb
                                              
      

tt=['C',0.35,'G',0.35,'A',0.15,'T',0.15]
tarea=[2,3,2,1,3,2,1,2]
tt2=[" 2C, 3G, 2A y 1T"," 3C, 2G, 1A y 2T"]

outf="RPaccotacya_Practica06_A.txt"
file_out=open(outf,"w")
for i in range(0,len(tarea)/4):
    
    resp="Probabilidad de que haya "+tt2[i]+" es "+\
          str(valeatn(tarea[i*4],tarea[i*4+1],tarea[i*4+2],tarea[i*4+3],\
            tt[1],tt[3],tt[5],tt[7]))
    print resp
    file_out.write(resp+'\n')
file_out.close()


