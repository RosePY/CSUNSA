#!/usr/bin/env python
# -*- coding: utf-8 -*-

#PRACTICA 03-A:
""" Cree un programa que lea 4 archivos practica_03A_1.txt,
practica_03A_2.txt, practica_03A_3.txt, practica_03A_4.txt
que contiene una secuencia de ADN y que define cual:
Cuál es la probabilidad de seleccionar una A.
Cuál es la probabilidad de seleccionar una T.
Cuál es la probabilidad de seleccionar una C.
Cuál es la probabilidad de seleccionar una G. """

s1="ACAGACAGATACAAT"

inf="practica_03A_"
listinf=[inf+str(i)+".txt" for i in range(1,5)]
print listinf
listadn=[]
adn=""
#""" Lectura y union de los archivos en un string"""
for w in listinf:
      for line in file(w):
          adn=adn+line
      adn=adn.replace('\n','')      
print adn

def prob(abc,char):
      """Probabilidad de char en abc"""
      return float(abc.count(char))/float(len(abc))
tarea=['A','T','C','G'] 
probs=[prob(adn,i) for i in tarea]
print "\n".join( ["Probabilidad de "+tarea[i]+": " +str(probs[i]) \
                  for i in range(0,4)])

outf="RPaccotacya_Practica03_A.txt"
file_out=open(outf,"w")
file_out.write('\n'.join(map(str,probs)))
file_out.close()


