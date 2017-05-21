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

ss="ACGTTGCA"


inf="practica_07.txt"
adn=""
for line in file(inf):
    adn=adn+line
adn=adn.replace('\n','')
print adn

def ccount(abc,cad):
    count=0
    for char in range(len(abc)):
        count += abc[char: char + len(cad)] == cad
    return count

def fact(n):
    return math.factorial(n)
def prob(abc,char):
      """Probabilidad de char en abc"""
      return float(abc.count(char))/float(len(abc))

nucl=['A','G','C','T']
nn=[ adn.count(e) for e in nucl]
pesos=[[10,-1,-3,-4],[-1,7,-5,-3],[-3,-5,9,0],[-4,-3,0,8]]

def cmatr(cad1,cad2):
    a=[]
    for i in range(len(cad1))
        for j in range(len(cad2))

pn=[prob(adn,n) for n in nucl]
def matr(adn):
    nnm=[nn[it]-(1 if adn[-1]==nucl[it] else 0) for it in range(0,4) ]
    #print nnm
    a=[ ]
    for i in range(0,4):
        b=[]
        for j in nucl:
            b.append(float(ccount(adn, nucl[i]+j))/nnm[i])
        a.append(b)
    #print a
    return a

def probcad(adn,cad):
    matriz=matr(adn)
    #print matriz
    ini=prob(adn,cad[0])
    #print ini
    values=[0,1,2,3]
    dd=dict(zip(nucl, values))
    iii=0
    temp=1
    for i in cad[0:len(cad)-1]:
        #print i,cad[iii+1]
        proba=matriz[dd[i]][dd[cad[iii+1]]]
        #print proba
        temp*=proba
        iii+mat=1
    return ini*temp

print matr(adn)
print probcad(adn,"ACGT") 
resp=["ATCA","CAGG","GAAT","TGAC"]
resp2=["Probabilidad de "+st+ " : " +str(probcad(adn,st)) for st in resp]
#print resp2
outf="RPaccotacya_Practica07.txt"
file_out=open(outf,"w")
print '\n'.join(resp2)
file_out.write('\n'.join(resp2))
file_out.close()



