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

    

def anw(mm,ma,g,cad1,cad2): #cad1<
    im=0
    jm=0
    may=0
    a=[]
    for i in range(len(cad1)+1):
        a.append([])
        for j in range(len(cad2)+1):
            if i==0:
                a[i].append(0)
            elif j==0:
                a[i].append(0)
            else:
                a[i].append(0)
    print a
    v=g
    for i in range(1,len(cad1)+1):
        for j in range(1,len(cad2)+1):
            #print a[i-1][j-1]
            diag=a[i-1][j-1]+ (ma if cad1[i-1]==cad2[j-1] else mm)
            
            izq=a[i][j-1]+v
            arr=a[i-1][j]+v
            #print diag,izq,arr
            a[i][j]=max(diag,izq,arr,0)
            if a[i][j]>=may:
                im=i
                jm=j
                may=a[i][j]
    print may,im,jm
    for i in range(len(cad1)+1):
        print a[i],"\n"
    m=a
    fit1=""
    fit2=""
    i=im
    j=jm

    while(i!=0 or j!=0):
        print m[i][j],m[i][j-1]+g, m[i-1][j-1]+(ma if cad1[i-1]==cad2[j-1] else mm ),
        if(m[i][j]==m[i-1][j-1]+(ma if cad1[i-1]==cad2[j-1] else mm)):
            print "d"
            fit1+=cad2[j-1]
            fit2+=cad1[i-1]
            i-=1
            j-=1
            print fit1,fit2,i,j

        elif(m[i][j]==m[i][j-1]+v):# izq
            print "i"
            fit1+=cad2[j-1]
            fit2+="_"
            j-=1
            print fit1,fit2,i,j
 
        else:
            print "a"
            fit2+=cad1[i-1]
            fit1+="_"
            i-=1
            print fit1,fit2,i,j
        if m[i][j]==0:
             break

    
    print fit2[::-1]
    print fit1[::-1]
        


a1="CGTCTT"
a2="ACCGTCTT"
a3="GTACATCC"
a4="TACA"
a5="CAGTATCGT"

a6="GTACGTATC"
a7="GGATCGA"
a8="GAATTCAGTTA"

anw(-1,+1,-1,"GAT","GGAT") 
