#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
"""Cree un programa que lea dos archivos practica01A_1.txt y
practica01A_2.txt que lea una secuencia de ADN, realice la
transcripción, la traducción y determine los aminoácidos en la
cadena."""
nucl={'A':'Adenina','T':'Timina', 'C': 'Citosina','G':'Guanina'}
purinas=['A','G']
pirimidina=['C','T','U']


s1="ACAGACAGATACAAT"

def transcripcion(A):
      return A.replace('T','U')

inf1= "practica01A_1.txt"
inf2="practica01A_2.txt"

outf1="RPaccotacya_Practica01_A_1.txt"
outf2="RPaccotacya_Practica01_A_2.txt"



def lect_codones():
      a=[]
      with open('codones.csv','rU') as f:
            rows = csv.reader(f)
            next(rows)                      
            for r in rows:
                  #print r
                  a.append(r)
      return a

def traduccion(ifi,ofi):
      file_out=open(ofi,"w")
      arn=""
      for line in file(ifi):
            arn=arn+line
      arn=arn.replace('\n','')
      arn=transcripcion(arn)
      codones= lect_codones()
      if len(arn)%3!=0:
            print "Cadena incompleta, no modulo de 3"
      else:
            codons=[]
            for i in range(0,len(arn),3):
                  codons.append(arn[i:i+3])
            ami=[]
            for i in codons:
                  for j in codones:
                        if i==j[0]:
                              ami.append(j[3])
                              ami.append("("+j[2]+")")
            
            print ami
                              
            file_out.write(" ".join(ami))

traduccion(inf1,outf1)
