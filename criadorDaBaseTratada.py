from difflib import SequenceMatcher
from unidecode import unidecode
import csv

capitais=open("dados/capitais.csv", 'r')
capitais=capitais.readlines()
i = 0
while i<len(capitais):
  capitais[i]=capitais[i].strip().split(';')
  capitais[i][1]=unidecode(capitais[i][1].lower())
  i+=1
capitais[0]=["UF","municipio","região"]


frota=open("dados/frota_munic_modelo_julho_2021.csv",'r')
frota=frota.readlines()
x=0
Frota=[]
nomeFrota=[]
while x<len(frota):
  frota[x]=frota[x].split(';')
  Frota+=[[frota[x][0],unidecode(frota[x][1].lower()),frota[x][2].strip()]]
  nomeFrota+=[[Frota[x][0],Frota[x][1]]]
  x+=1
Frota[0][1],nomeFrota[0][1]="municipio","municipio"

### Falta:
#
#   Ler e tratar o arquivo da população
#   Comparar os nomes de municípios das listas de população e frota
#     Nos nomes parecidos, usar o SequenceMatcher
#     Nos nomes muito diferentes, criar uma lista com as incongruências
#   Criar o csv com UF, município, macrorregião, população, frota
###