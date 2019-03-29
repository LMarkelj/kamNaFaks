import requests
import Razredi
import re





def ustvariProgramMar(naslovStrani,ime_programa):
    '''Ustvari in vrne Študijski program,z njegovimi predmeti'''
    novSez=[]
    stran = requests.get(naslovStrani).text
    stran = re.split(r'<table class="predmetniki" border="0" cellspacing="0" cellpadding="0">',stran)
    stran = stran[1:-2]
    for i in range(len(stran)):
        stran[i] = re.split("<tr>",stran[i])
        stran[i] = stran[i][4:]
        for j in range(len(stran[i])):

            stran[i][j] = re.split("<td>",stran[i][j])
            stran[i][j] = stran[i][j][2:]
            stran[i][j] = [stran[i][j][0],stran[i][j][-3],stran[i][j][-1]]
            stran[i][j][0] = odstrani_html(stran[i][j][0])
            stran[i][j][1] = stran[i][j][1].split("<")[0]
            stran[i][j][2] = stran[i][j][2].split("<")[0].split("/")[1]
    print(stran)



ustvariProgramMar("https://www.fnm.um.si/index.php/2019/02/04/fizika-predmetnik-s-kreditnim-ovrednotenjem-studijskih-obveznosti-2019-2020/","fizika")