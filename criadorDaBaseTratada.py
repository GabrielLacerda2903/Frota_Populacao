from difflib import SequenceMatcher as sm
from unidecode import unidecode

capitais=open("dados/capitais.csv", 'r')
capitais=capitais.readlines()
i = 0
while i<len(capitais):
  capitais[i]=capitais[i].strip().split(';')
  capitais[i][1]=unidecode(capitais[i][1].lower())
  i+=1
capitais[0]=["UF","municipio","regiao"]


Frota=open("dados/frota_munic_modelo_julho_2021.csv",'r').readlines()
x=0
frota=[]
nomeFrota=[]
while x<len(Frota):
  Frota[x]=Frota[x].split(';')
  frota+=[[Frota[x][0],unidecode(Frota[x][1].lower()),Frota[x][2].strip()]]
  nomeFrota+=[[frota[x][0],frota[x][1]]]
  x+=1
frota[0]=['UF','municipio','frota total']
nomeFrota[1]=['UF','municipio']

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
    k=pop[x][4].split("(")[0].split(".")
    m=int(k[0]+k[1])
  pop[x]=[pop[x][0],unidecode(pop[x][3]).lower(),m]
  nomePop+=[[pop[x][0],pop[x][1]]]
  x+=1
pop.remove([''])

soNaFrota=[]      ### cria uma lista de [UF,cidade] que tem no arquivo de frota, mas não no de população
for x in nomePop:
  try:
    nomeFrota.index(x)
  except:
    soNaFrota+=[x]

soNaPop=[]      ### mesma coisa do anterior, só que ao contrário
for x in nomeFrota:
  try:
    nomePop.index(x)
  except:
    soNaPop+=[[x[0],x[1],0,0]]

x=0
apagarPop=[]
while x<len(soNaPop):
  z=0
  while z<len(soNaFrota):       ### coloca a maior correspodencia que cada cidade tem
    s=sm(None,soNaPop[x][1], soNaFrota[z][1]).ratio()
    if x!=0 and s>soNaPop[x][2]:
      if soNaPop[x][0]==soNaFrota[z][0]:
        soNaPop[x][2],soNaPop[x][3]=s,soNaFrota[z][1]
    z+=1
  z=0
  while z<len(frota):
    if soNaPop[x][1] in frota[z] and soNaPop[x][0]==frota[z][0] and soNaPop[x][2]>0.5:
      frota[z][1]=soNaPop[x][3]
      apagarPop+=[x]
    z+=1
  x+=1

for x in reversed(apagarPop):
  soNaPop.pop(x)

arq=open('saidas/baseTratada.csv','w')
for i,x in enumerate(pop):
  for z in frota:
    if pop[i][0]==z[0] and pop[i][1]==z[1]:
      n=z[2]
  for w in capitais:
    if w[0]==pop[i][0]:
      m=w[2]
  arq.write(f'{m},{pop[i][0]},{pop[i][1]},{pop[i][2]},{n}\n')
arq.close()

arq=open('saidas/cidadeNaoEncontradas.csv','w')
arq.write('UF,municipio\n')
for x in soNaPop:
  arq.write(x[0]+','+x[1]+'\n')
arq.close()