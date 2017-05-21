#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
#PRACTICA 04-A:
""" De una cadena de ADN en un archivo practica_05_B.txt.
Cree un programa que responda:
Probabilidad de seleccionar una Purina en el segundo intento.
Probabilidad de seleccionar una Purina en el cuarto intento.
Probabilidad de seleccionar una Pirimidina en el tercero intento.
Probabilidad de seleccionar una Pirimidina en el quinto intento."""
nucl={'A':'Adenina','T':'Timina', 'C': 'Citosina','G':'Guanina'}
purinas=['A','G']
pirimidina=['C','T','U']

inf="practica_05_B.txt"
adn=""
for line in file(inf):
    adn=adn+line
adn=adn.replace('\n','')
print adn

def prob(abc,char):
      """Probabilidad de char en abc"""
      return float(abc.count(char))/float(len(abc))
def geom(n,pex):
    return ((1-pex)**(n-1))*pex

pp=sum(prob(adn,i) for i in purinas)
print pp
tarea=[2,4,3,5]
outf="RPaccotacya_Practica05_B.txt"
file_out=open(outf,"w")
n=["purina","pirimidina"]
for i in range(0,len(tarea)):
    
    resp="Probabilidad de seleccionar una "+(n[0] if i>1 else n[1])+\
                  " en "+str(tarea[i])+"intento es \t"+str(geom(tarea[i],pp))
    print resp
    file_out.write(resp+'\n')
file_out.close()


