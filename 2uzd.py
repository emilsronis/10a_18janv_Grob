import csv

def lacis():
    try:
        with open("datne.csv", 'r', encoding='utf-8') as dd:
            kakis = csv.reader(dd)
            for rinda in kakis:
                if len(rinda) > 1: 
                    print(rinda[1])

    except FileNotFoundError:
        print(f"Faila '{"datne.csv"}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

lacis('datne.csv')

if __name__=="__main__":
    lacis()