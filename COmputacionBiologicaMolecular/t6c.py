#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import numpy as np
#PRACTICA 06-C:
""" Implementar un programa que lea un archivo
practica_06C.txt que contenga una cadena de
ADN y calcule:
● Aproximadamente cuántos nucleótidos son retirados
de la cadena de ADN hasta obtener una purina.
● Aproximadamente cuántos nucleótidos son retirados
de la cadena de ADN hasta obtener una pirimidina"""
nucl={'A':'Adenina','T':'Timina', 'C': 'Citosina','G':'Guanina'}
purinas=['A','G']
pirimidina=['C','T']

ss="AAATTTTT"

inf="practica_06_C.txt"
adn=""
for line in file(inf):
    adn=adn+line
adn=adn.replace('\n','')
print ss

def fact(n):
    return math.factorial(n)
def prob(abc,char):
      """Probabilidad de char en abc"""
      return float(abc.count(char))/float(len(abc))

def vepur(adn,c):
    nval=sum(adn.count(c) for c in (['A','G'] if c==0 else ['C','T']) )
    #print nval
    prob=0
    for i in range(1,len(adn)-nval+1):
        
        #print "--------------i 3w ",i
        nval2=len(adn)-float(nval)
        len2=float(len(adn))
        a=1
        for j in range(1,i):
           
            a=a*float(nval2)/(len2)
            #print a
            nval2=nval2-1
            len2=len2-1
        #print "part ",a*float(nval)/len2
        prob=prob+i*a*float(nval/len2)
    return prob

resp="Purina "+ str(vepur(ss,0))+"\n"+"Pirimidina "+str(vepur(ss,1))


outf="RPaccotacya_Practica06_C.txt"
file_out=open(outf,"w")
print resp
file_out.write(resp)
file_out.close()



