#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
#PRACTICA 04-A:
""" La probabilidad de seleccionar una Purina de una cadena de
ADN es 0.35. Cree un programa que responda:
Si seleccionamos 40 Nucleótidos cuál es la probabilidad que halla
exactamente 8 Purinas.
Si seleccionamos 20 Nucleótidos cuál es la probabilidad que halla
exactamente 12 Purinas.
Si seleccionamos 30 Nucleótidos cuál es la probabilidad que halla
exactamente 11 Purinas.
Si seleccionamos 38 Nucleótidos cuál es la probabilidad que halla
exactamente 9 Pirimidinas.
Si seleccionamos 51 Nucleótidos cuál es la probabilidad que halla
exactamente 13 Pirimidinas."""
nucl={'A':'Adenina','T':'Timina', 'C': 'Citosina','G':'Guanina'}
purinas=['A','G']
pirimidina=['C','T','U']
def fact(n):
    return math.factorial(n)
def c(n,k):
    return fact(n)/(fact(k)*fact(n-k))
def prob(abc,char):
      """Probabilidad de char en abc"""
      return float(abc.count(char))/float(len(abc))
def binomial(n,k,pex):
    return c(n,k)*(pex**k)*((1-pex)**(n-k))

p=0.35
tarea=[40,8,p,20,12,p,30,11,p,38,9,1-p,51,13,1-p]
outf="RPaccotacya_Practica04_A.txt"
file_out=open(outf,"w")
n=["purinas","pirimidinas"]
for i in range(0,5):
    
    resp="Probabilidad de "+str(tarea[3*i+1])+" "+(n[0] if i>2 else n[1])+\
                  " en "+str(tarea[3*i])+" nucleotidos es \t"+str(float( binomial(tarea[3*i],tarea[3*i+1],tarea[3*i+2])))
    print resp
    file_out.write(resp+'\n')
file_out.close()


