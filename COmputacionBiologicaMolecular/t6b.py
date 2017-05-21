#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
#PRACTICA 06-B:
""" De una cadena de ADN en un archivo practica_05_B.txt.
Cree un programa que responda:
Probabilidad de seleccionar una Purina en el segundo intento.
Probabilidad de seleccionar una Purina en el cuarto intento.
Probabilidad de seleccionar una Pirimidina en el tercero intento.
Probabilidad de seleccionar una Pirimidina en el quinto intento."""
nucl={'A':'Adenina','T':'Timina', 'C': 'Citosina','G':'Guanina'}
purinas=['A','G']
pirimidina=['C','T','U']

inf="practica_06_B.txt"
adn=""
for line in file(inf):
    adn=adn+line
adn=adn.replace('\n','')
print adn

def fact(n):
    return math.factorial(n)
def prob(abc,char):
      """Probabilidad de char en abc"""
      return float(abc.count(char))/float(len(abc))

def valeatn(a,b,c,d,pa,pb,pc,pd):
      return (pa**a)*(pb**b)*(pc**c)*(pd**d)*fact(a+b+c+d)/(fact(a)*fact(b)*fact(c)*fact(d))
      

tt=['C',0.35,'G',0.35,'A',0.15,'T',0.15]
for i in range(0,4):
    tt[i*2+1]=prob(adn,tt[i*2])
print tt
tarea=[3,4,2,4,2,3,2,3,1,2,3,2,2,1,3,1]
text=['C','G','A','T']


outf="RPaccotacya_Practica06_B.txt"
file_out=open(outf,"w")
for i in range(0,len(tarea)/4):
    cad=str(tarea[i*2])+text[0]+", "+str(tarea[i*2+1])+text[1]+", "+str(tarea[i*2+2])+text[2]+", "+str(tarea[i*2+3])+text[3]
    resp="Probabilidad de que haya "+cad+" es "+\
          str(valeatn(tarea[i*4],tarea[i*4+1],tarea[i*4+2],tarea[i*4+3],\
            tt[1],tt[3],tt[5],tt[7]))
    print resp
    file_out.write(resp+'\n')
file_out.close()

