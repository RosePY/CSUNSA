import csv

nucl={'A':'Adenina','T':'Timina', 'C': 'Citosina','G':'Guanina'}
purinas=['A','G']
pirimidina=['C','T','U']

s1="ACAGACAGATACAAT"

def transcripcion_rev(A):
      return A.replace('U','T')

inf=["1cq0","1j6z","1ron","2v26"]

outf="RPaccotacya_Practica01_B.txt"
file_out=open(outf,"w")

      

def lect_codones():
      a=[]
      with open('codones.csv','rU') as f:
            rows = csv.reader(f)
            next(rows)                      
            for r in rows:
                  #print r
                  a.append(r)
      return a

def traduccion_rev(ifi):
      prot=""
      for line in file(ifi):
            prot=prot+line
            
      prot=prot.replace('\n','')
      print prot
      codones= lect_codones()
      codons=""
      for i in range(len(prot)):
            
            for j in codones:
                  if prot[i]==j[3]:
                        codons+=j[0]
                        #print "ebtro"
      print codons      
      file_out.write(codons)#transcripcion_rev(codons))
      file_out.write('\n')

for i in inf:
      traduccion_rev(i+".fasta.txt")
