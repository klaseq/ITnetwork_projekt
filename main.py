from pojistenec import Pojistenec
from seznam import Seznam

def menu():
    print("=========================\nEvidence pojistenych\n=========================")
    print("Vyber akci:")
    print("\t1 - pridat noveho pojistence")
    print("\t2 - vypsat vsechny pojistence")
    print("\t3 - vyhledat pojistence")
    print("\t4 - konec")

seznam = Seznam()

while True:
    menu()
    try:
        vyber = int(input("Zadej operaci: "))
        if vyber < 1 or vyber > 4:
            raise Exception("Bylo zvoleno spatne cislo")
    except Exception as e:
        print(e)
        print("Prosim vyber validni cislo z menu")

    if vyber == 4:
        print("Program byl ukoncen")
        break
    elif vyber == 1:
        seznam.pridat()
        tlacitko = input("data byla ulozena, pokracujte libovolnou klavesou...")
    elif vyber == 2:
        print("seznam pojistenych:")
        print("\t-----------------------------------------------")
        for pojistenec in seznam.pojistenci:
            print("\t", pojistenec)
        print("\t-----------------------------------------------")
        tlacitko = input("pokracujte libovolnou klavesou...")
    elif vyber == 3:
        seznam.vyhledat()