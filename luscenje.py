import re
import requests
from Razredi import *



stran = requests.get('http://www.ung.si/sl/studij/fakulteta-za-naravoslovje/studij/1FAF/').text 
#prebere stran 

tabela = re.split(r'<table class="table table-hover">', stran)[2:]

for i in range(len(tabela)):
    tabela[i] = re.split(r'<tr>', tabela[i]) #pregleda tabele in splita po <td>
    for j in range(len(tabela[i])):
        tabela[i][j] = re.split(r'</td>', tabela[i][j])
        for k in range(len(tabela[i][j])):
            tabela[i][j][k] = odstrani_html(tabela[i][j][k]).strip('\n').lstrip(' ') #odstrani vse ''white space''
            


            
           
            
print(tabela)