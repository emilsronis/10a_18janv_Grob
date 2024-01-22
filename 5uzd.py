def ieraksti_vardu():
    vards = input("Ievadiet savu vārdu: ")
    return vards

def ierakstit_faila(vards, pulkstenis):
    try:
        with open(pulkstenis, 'w') as fails:
            fails.write(vards)
        print(f"Vārds '{vards}' veiksmīgi ierakstīts failā '{pulkstenis}'.")

    except IOError as e:
        print(f"Kļūda: Nevarēja ierakstīt failā '{pulkstenis}'. {e}")
        
    except Exception as e:
        print(f"Radās kļūda: {e}")

def main():
    pulkstenis = "lietotajs.txt"

    vards = ieraksti_vardu()
    ierakstit_faila(vards, pulkstenis)

if __name__ == "__main__":
    main()
