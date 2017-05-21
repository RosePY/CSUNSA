#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
#PRACTICA 04-A:
""" De una cadena de ADN en un archivo practica_04_B.txt.
Cree un programa que responda:
Si seleccionamos 10 Nucleótidos cuál es la probabilidad que halla
exactamente 5 Purinas.
Si seleccionamos 15 Nucleótidos cuál es la probabilidad que halla
exactamente 7 Purinas.
Si seleccionamos 13 Nucleótidos cuál es la probabilidad que halla
exactamente 6 Pirimidinas.
Si seleccionamos 12 Nucleótidos cuál es la probabilidad que halla
exactamente 3 Pirimidinas."""
nucl={'A':'Adenina','T':'Timina', 'C': 'Citosina','G':'Guanina'}
purinas=['A','G']
pirimidina=['C','T','U']

inf="practica_04_B.txt"
adn=""
for line in file(inf):
    adn=adn+line
adn=adn.replace('\n','')
print adn

def fact(n):
    return math.factorial(n)
def c(n,k):
    return fact(n)/(fact(k)*fact(n-k))
def prob(abc,char):
      """Probabilidad de char en abc"""
      return float(abc.count(char))/float(len(abc))
def binomial(n,k,pex):
    return c(n,k)*(pex**k)*((1-pex)**(n-k))

pp=sum(prob(adn,i) for i in purinas)
t=len(adn)
tarea=[10,5,pp,15,7,pp,13,6,1-pp,12,3,1-pp]
outf="RPaccotacya_Practica04_B.txt"
file_out=open(outf,"w")
n=["purinas","pirimidinas"]
for i in range(0,4):
    
    resp="Probabilidad de "+str(tarea[3*i+1])+" "+(n[0] if i>1 else n[1])+\
                  " en "+str(tarea[3*i])+" nucleotidos es \t"+str(float( binomial(tarea[3*i],tarea[3*i+1],tarea[3*i+2])))
    print resp
    file_out.write(resp+'\n')
file_out.close()


