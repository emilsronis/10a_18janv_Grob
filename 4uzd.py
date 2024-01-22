def puke():
    try:
        with open(puke, 'r') as fails:
            saturs = fails.read()
            print("Faila saturs:")
            print(saturs)

    except FileNotFoundError:
        print(f"Kļūda: Fails ar nosaukumu '{puke}' nav atrasts.")
    except Exception as e:
        print(f"Radās kļūda: {e}")

def main():
    nosaukums = input("Ievadiet faila nosaukumu: ")
    formats = input("Ievadiet faila formātu (paplašinājumu): ")

    puke = f"{puke.txt}.{'txt'}"

    puke()

if __name__ == "__main__":
    main()
