import csv

nucl={'A':'Adenina','T':'Timina', 'C': 'Citosina','G':'Guanina'}
purinas=['A','G']
pirimidina=['C','T','U']

s1="ACAGACAGATACAAT"

inf="practica_02A.txt"
adn=""
for line in file(inf):
    adn=adn+line
    
adn=adn.replace('\n','')
print adn

outf="EHinojosa_Practica02_A.txt"
file_out=open(outf,"w")

def prob(abc,char):

      return float(abc.count(char))/float(len(abc))

probs=[prob(adn,i) for i in ['A','T','C','G'] ]
      
print probs
probs.append(probs[0]+probs[-1])
probs.append(probs[1]+probs[2])
print probs
print map(str,probs)
file_out.write('\n'.join(map(str,probs)))
file_out.close()

