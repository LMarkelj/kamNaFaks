class Predmet():
    '''Hrani podatke o predmetu'''
    def __init__(self,ime,ure,kreditneT):
        '''pocisti kodo in zavaruj'''
        self.ime=ime
        self.ure=ure
        self.kreditneT=kreditneT
    
class Program():
    '''hrani podatke o programu'''
    def __init__(self,ime,stopnja,predmeti):
        '''Zavaruj'''
        self.predmeti=predmeti
        self.ime=ime
        self.stopnja=stopnja

class Fakulteta():
    '''Hrani podatke o fakulteti'''
    def __init__(self,ime,programi):
        '''zavaruj'''
        self.ime=ime
        self.programi=programi







def odstrani_html(tekst):
    '''V danem tekstu odstrani kodo zajeto v <>'''
    novobesedilo = ""
    oznaka = 0
    for znak in tekst:
        if znak == "<":
            oznaka = 1
        elif znak == ">":
            oznaka = 0
        elif oznaka == 0:
            novobesedilo += znak
    return novobesedilo










