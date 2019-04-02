import re
import requests
from Razredi import *

def preberi_stran(stran_html, ime, stopnja):
    '''prebere podatke iz html-ja '''
    nov_seznam = []
    stran = requests.get(stran_html).text 
    #prebere stran 
    tabela = re.split(r'<table class="table table-hover">', stran)[2:]
    for i in range(len(tabela)):
        tabela[i] = re.split(r'<tr>', tabela[i])[1:] #pregleda tabele in splita po <td>
        for j in range(len(tabela[i])):
            tabela[i][j] = re.split(r'</td>', tabela[i][j])
            for k in range(len(tabela[i][j])):
                tabela[i][j][k] = odstrani_html(tabela[i][j][k]).strip('\n').lstrip(' ').replace("\n", "").rstrip(" ").lstrip(" ") #odstrani vse ''white space''
            nov_seznam.append(Predmet(tabela[i][j][0], tabela[i][j][1], tabela[i][j][2]))
    tabela[-1][-1][-1] = 0 #namesto zadnjega dela html-ja zapiše 0
    return Program(ime, stopnja, nov_seznam) 


preberi_stran('http://www.ung.si/sl/studij/fakulteta-za-naravoslovje/studij/1FAF/', 'fizika Nova Gorica', '1')


def ime_fakultete():
    programi=[preberi_stran('http://www.ung.si/sl/studij/fakulteta-za-naravoslovje/studij/1FAF/', 'fizika Nova Gorica', '1')]
    ime = 'Fakulteta za naravoslovje'
    return Fakulteta(ime, programi)
