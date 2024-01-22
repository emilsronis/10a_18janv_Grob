import csv

def lacis():
    try:
        with open("zieds.csv", 'r', encoding='utf-8') as dd:
            kakis = csv.reader(dd)
            for rinda in kakis:
                if len(rinda) > 2: 
                    print(rinda[2])

    except FileNotFoundError:
        print(f"Faila '{"zieds.csv"}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")



if __name__=="__main__":
    lacis()