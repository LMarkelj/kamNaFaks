class Predmet():
    '''Hrani podatke o predmetu'''
    def __init__(self,ime,vaje,predavanja,kreditneT):
        '''pocisti kodo in zavaruj'''
        self.ime=ime
        self.vaje=vaje
        self.predavanja=predavanja
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

kr



