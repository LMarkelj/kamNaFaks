import Razredi
import fizMar
#import luscenje

def dobi_podatke():
    '''funkcija vrne seznam vseh faksov'''
    sezF = []
    sezF.append(fizMar.inciliziraj_mar())

    return sezF


def izpisVsega(sezF):
    '''izpise vse fakse in programe'''
    for element in sezF:
        print(element)




def main():
    sezF = dobi_podatke()
    izbira = int(input('1. Izpiši vse fakse ter njihove programe\n2. Najdi vse fakse ki imajo dani predmet\n3. Zapri program\n Izberite: '))
    if izbira == 1:
        izpisVsega(sezF)
    elif izbira == 2:
        print("V delu 2")
    elif izbira == 3:
        pass


main()