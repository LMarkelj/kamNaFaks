import re
import requests
import Razredi



stran = requests.get('http://www.ung.si/sl/studij/fakulteta-za-naravoslovje/studij/1FAF/').text 
#prebere stran 

tabela = re.split(r'<table class="table table-hover">', stran)[2:]

for i in range(len(tabela)):
    tabela[i] = re.split(r'<tr>', tabela[i])[1:]
    for j in range(len(tabela[i])):
        tabela[i][j] = re.split(r'<td>', tabela[i][j])[1:]




    
print(tabela)