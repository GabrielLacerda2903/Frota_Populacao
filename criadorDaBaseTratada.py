from difflib import SequenceMatcher as sm
from unidecode import unidecode

capitais=open("dados/capitais.csv", 'r')
capitais=capitais.readlines()
i = 0
while i<len(capitais):
  capitais[i]=capitais[i].strip().split(';')
  capitais[i][1]=unidecode(capitais[i][1].lower())
  i+=1
capitais[0]=["UF","municipio","região"]


Frota=open("dados/frota_munic_modelo_julho_2021.csv",'r').readlines()
x=0
frota=[]
nomeFrota=[]
while x<len(Frota):
  Frota[x]=Frota[x].split(';')
  frota+=[[Frota[x][0],unidecode(Frota[x][1].lower()),Frota[x][2].strip()]]
  nomeFrota+=[[frota[x][0],frota[x][1]]]
  x+=1
frota[0][1],nomeFrota[0][1]="municipio","municipio"

Pop=open("dados/POP2021_20221212.csv",'r')
Pop.readline()
x=1
pop=[["UF","municipio","populacao"]]
nomePop=[["UF","municipio"]]
while 1:
  pop+=[Pop.readline().split(";")]
  if pop[x]==['']:
    break
  try:
    m=int(pop[x][4].strip())
  except:
    m=pop[x][4].split("(")[0]
  pop[x]=[pop[x][0],unidecode(pop[x][3]).lower(),m]
  nomePop+=[[pop[x][0],pop[x][1]]]
  x+=1
pop.remove([''])

soNaFrota=[]      ### cria uma lista de [UF,cidade,0] que tem no arquivo de frota, mas não no de população
for x in nomePop:
  try:
    nomeFrota.index(x)
  except:
    soNaFrota+=[x]

soNaPop=[]      ### mesma coisa do anterior
for x in nomeFrota:
  try:
    nomePop.index(x)
  except:
    soNaPop+=[[x[0],x[1],0]]

x=0       ### coloca a maior correspodencia que cada cidade tem
while x<len(soNaPop):
  z=0
  while z<len(soNaFrota):
    s=sm(None,soNaPop[x][1], soNaFrota[z][1]).ratio()
    if s>soNaPop[x][2]:
      if soNaPop[x][0]==soNaFrota[z][0]:
        n=s
        soNaPop[x][2]=s
    z+=1
  x+=1

print(soNaPop)

### Falta:
#   Comparar os nomes de municípios das listas de população e frota
#     Nos nomes parecidos, usar o SequenceMatcher
#     Nos nomes muito diferentes, criar uma lista com as incongruências
#   Criar o csv com UF, município, macrorregião, população, frota
###