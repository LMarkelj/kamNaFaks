import requests
from Razredi import *
import re


def ustvariProgramMar(naslovStrani,ime_programa,stopnja):
    '''Ustvari in vrne Študijski program,z njegovimi predmeti'''
    novSez=[]
    stran = requests.get(naslovStrani).text
    stran = re.split(r'<table class="predmetniki" border="0" cellspacing="0" cellpadding="0">',stran)
    stran = stran[1:]
    for i in range(len(stran)):
        stran[i] = re.split("<tr>",stran[i])
        stran[i] = stran[i][4:]
        for j in range(len(stran[i])):
            stran[i][j] = re.split("<td>",stran[i][j])
            stran[i][j] = stran[i][j][2:]
            stran[i][j] = [stran[i][j][0],stran[i][j][-3],stran[i][j][-1]]
            stran[i][j][0] = odstrani_html(stran[i][j][0]).strip('\n')
            stran[i][j][1] = stran[i][j][1].split("<")[0]
            stran[i][j][2] = stran[i][j][2].split("<")[0].split("/")[1]
            if stran[i][j][0] !='Izbirni predmet' and stran[i][j][0] != 'Prostoizbirni predmet**' and stran[i][j][0] !='Skupaj':
                novSez.append(Predmet(stran[i][j][0],stran[i][j][1],stran[i][j][2]))
    return Program(ime_programa,stopnja,novSez)

def ustvari_faks_mar(ime,programi):
    '''Funkcija zapise podatke o faksu v primeren class in ga vrne'''
    return Fakulteta(ime,programi)


def inciliziraj_mar():
    return ustvari_faks_mar("Maribor fizika",[ustvariProgramMar("https://www.fnm.um.si/index.php/2019/02/04/fizika-predmetnik-s-kreditnim-ovrednotenjem-studijskih-obveznosti-2019-2020/","fizika",1)])

