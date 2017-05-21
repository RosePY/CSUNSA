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

nucl=['A','G','C','T']

pesos=[[10,-1,-3,-4],[-1,7,-5,-3],[-3,-5,9,0],[-4,-3,0,8]]

def cmatr(cad1,cad2): #cad1<
    a=[]
    for i in range(len(cad1)+1):
        a.append([])
        for j in range(len(cad2)+1):
            if i==0:
                a[i].append(j*-5)
            elif j==0:
                a[i].append(i*-5)
            else:
                a[i].append(0)

    values=[0,1,2,3]
    dd=dict(zip(nucl, values))
    v=-5
    for i in range(1,len(cad1)+1):
        
        for j in range(1,len(cad2)+1):
            diag=a[i-1][j-1]+pesos[dd[cad1[i-1]] ][dd[cad2[j-1]] ]
            izq=a[i][j-1]+v
            arr=a[i-1][j]+v
            a[i][j]=max(diag,izq,arr)
    for i in range(len(cad1)+1):
        print a[i],"\n"
    return a

def anw(cad1,cad2):
    m=cmatr(cad1,cad2)
    fit1=""
    fit2=""
    i=len(cad1)
    j=len(cad2)
    values=[0,1,2,3]
    dd=dict(zip(nucl, values))
    while(i!=0 or j!=0):
        if(m[i][j]==m[i-1][j-1]+pesos[dd[cad1[i-1]] ][dd[cad2[j-1]] ]):
            fit1+=cad2[j-1]
            fit2+=cad1[i-1]
            i-=1
            j-=1
        elif(m[i][j]==m[i][j-1]-5):
            fit1+=cad2[j-1]
            fit2+="_"
            j-=1
        else:
            fit2=cad1[i-1]
            fit1+="_"
            i-=1
    print fit1[::-1]
    print fit2[::-1]
        


a1="CGTCTT"
a2="ACCGTCTT"
a3="GTACATCC"
a4="TACA"
anw(a1,a2) 
