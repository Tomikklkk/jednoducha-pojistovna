from pojistovna import Pojistovna

pojistovna = Pojistovna()

while True:
    print("-----------------------")
    print("Evidence pojištěných")
    print("-----------------------")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného")
    print("4 - Konec")

    volba = input("Vyberte si akci:\n")

    if volba == "1":
        jmeno = input("Zadejte jméno pojištěného:\n")
        prijmeni = input("Zadejte příjmení:\n")
        telefon = input("Zadejte telefoní číslo:\n")
        vek = int(input("Zadjete věk:\n"))
        pojistovna.pridej_zakaznika(jmeno, prijmeni, telefon, vek)

    elif volba == "2":
        pojistovna.vypis_vsechny_zakazniky()

    elif volba == "3":
        jmeno = input("Zadejte jméno pojištěného:\n")
        prijmeni = input("Zadejte příjmení:\n")
        pojistovna.vyhledej_zakaznika(jmeno, prijmeni)

    elif volba == "4":
        break

    else:
        print("Neplatná volba. Zadejte číslo 1-4.")