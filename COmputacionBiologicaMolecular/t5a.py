#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
#PRACTICA 04-A:
""" En una secuencia de ADN los nucleótidos C, G, A y T ocurren
con frecuencias (o proporciones) 19/100, 31/100, 37/100 y
13/100 respectivamente. Cree un programa que responda:
Probabilidad de seleccionar una Purina en el tercero intento.
Probabilidad de seleccionar una Purina en el quinto intento.
Probabilidad de seleccionar una Purina en el séptimo intento.
Probabilidad de seleccionar una Purina en el noveno intento.
Probabilidad de seleccionar una Pirimidina en el cuarto intento.
Probabilidad de seleccionar una Pirimidina en el sexto intento.
Probabilidad de seleccionar una Pirimidina en el octavo intento.
Probabilidad de seleccionar una Pirimidina en el décimo intento."""
nucl={'A':'Adenina','T':'Timina', 'C': 'Citosina','G':'Guanina'}
purinas=['A','G']
pirimidina=['C','T','U']

def prob(abc,char):
      """Probabilidad de char en abc"""
      return float(abc.count(char))/float(len(abc))
def geom(n,pex):
    return ((1-pex)**(n-1))*pex

tt=['C',0.19,'G',0.31,'A',0.37,'T',0.13]
tarea=[3,5,7,9,4,6,8,10]
pp=0.68

outf="RPaccotacya_Practica05_A.txt"
file_out=open(outf,"w")
n=["purina","pirimidina"]
for i in range(0,8):
    
    resp="Probabilidad de seleccionar una "+(n[0] if i>3 else n[1])+\
                  " en "+str(tarea[i])+"intento es \t"+str(geom(tarea[i],pp))
    print resp
    file_out.write(resp+'\n')
file_out.close()


