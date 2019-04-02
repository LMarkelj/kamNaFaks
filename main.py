import Razredi
import fizMar
import luscenje

def dobi_podatke():
    '''funkcija vrne seznam vseh faksov'''
    sezF = []
    sezF.append(fizMar.inciliziraj_mar())
    sezF.append(luscenje.ime_fakultete())

    return sezF

def izpisVsega(sezF):
    '''izpise vse fakse in programe'''
    for faks in sezF:
        print(faks)

def iskanjePoPredmetu(sezF,imePredmeta):
    '''Funkcija izpise vse fakse z danim predmetom'''
    for faks in sezF:
        zeNapisan = 0
        for program in faks.programi:
            for predmet in program.predmeti:
                if predmet.ime == imePredmeta:
                    print (faks.ime)
                    zeNapisan = 1
                    break
            if zeNapisan == 1:
                break






def main():
    sezF = dobi_podatke()
    izbira = int(input('1. Izpiši vse fakse ter njihove programe\n2. Najdi vse fakse ki imajo dani predmet\n3. Zapri program\n\nIzberite: '))
    if izbira == 1:
        izpisVsega(sezF)
    elif izbira == 2:
        imePredmeta = input("Vpišite ime predmeta: ")
        iskanjePoPredmetu(sezF,imePredmeta)
    elif izbira == 3:
        pass


main()