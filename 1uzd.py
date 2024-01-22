def lasit_datni():
    try:
        with open("aste.txt", 'r', encoding='utf-8') as datne:
            saturs=datne.readlines()
            print(saturs)



    except FileNotFoundError:
        print("Datne nav atrasta!")

if __name__=="__main__":
    lasit_datni()