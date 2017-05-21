#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Práctica 03-B
"""Cree un programa que lea 4 archivos practica_03B_1.txt,
practica_03B_2.txt, practica_03B_3.txt, practica_03B_4.txt
que contiene una secuencia de ADN y que define cual:
Cuál es la probabilidad de seleccionar una A de la 1ra cadena.
Cuál es la probabilidad de seleccionar una A de la 2da cadena,...,G,C,T """


ss=["ACAGACAGATACAAT","ACAGACAGATACAAT","ACAGACAGATACAAT"]

inf="practica_03B_"
listinf=[inf+str(i)+".txt" for i in range(1,5)]
listadn=[]
for w in listinf:
      adn=""
      for line in file(w):
          adn=adn+line
      adn=adn.replace('\n','')
      listadn.append(adn)
print listadn

def prob(char,abc):
      return float(abc.count(char))/float(len(abc))

def bayes(B,A,total): #Probab de q ocurra A en la particion B del total
      a=(1/float(len(total)))
      #print a
      aa=a*prob(A,total[B-1])
      #print aa
      b= sum(float(a)*prob(A,e) for e in total)
      return aa/b

tar1=['A','G','C','T']

outf="EHinojosa_Practica03_B.txt"
file_out=open(outf,"w")
for it in tar1:
      result= [ bayes(num,it,listadn) for num in range(1,5)]
      #print result
      print "\n".join( ["Probabilidad de "+it+" en "+listinf[i]+": " \
                        +str(result[i]) for i in range(0,4)])
      file_out.write('\n'.join(map(str,result)))
      file_out.write('\n')
#file_out.write('\n'.join(map(str,result)))
file_out.close()



