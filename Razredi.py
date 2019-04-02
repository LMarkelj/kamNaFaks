class Predmet():
    '''Hrani podatke o predmetu'''
    def __init__(self,ime,ure,kreditneT):
        '''pocisti kodo in zavaruj'''
        self.ime=ime
        self.ure=ure
        self.kreditneT=kreditneT
    
    def __repr__(self):
        return "{0}     {1}     {2}".format(self.ime,self.ure,self.kreditneT)
    
class Program():
    '''hrani podatke o programu'''
    def __init__(self,ime,stopnja,predmeti):
        '''Zavaruj'''
        self.predmeti=predmeti
        self.ime=ime
        self.stopnja=stopnja
    
    def __repr__(self):
        novniz="{0}, Stopnja: {1} \n".format(self.ime,self.stopnja).upper()
        for predmet in self.predmeti:
            novniz += predmet.__repr__()+"\n"
        return novniz
    

class Fakulteta():
    '''Hrani podatke o fakulteti'''
    def __init__(self,ime,programi):
        '''zavaruj'''
        self.ime=ime
        self.programi=programi

    def __repr__(self):
        novniz=self.ime.upper().bold()+"\n\n"
        for program in self.programi:
            novniz+=self.programi.__repr__()+"\n"








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










