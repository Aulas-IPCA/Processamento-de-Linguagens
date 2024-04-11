# Abrindo um ficheiro e salvando informações no mesmo
if False:
    data = "Hoje a aula é na sala T.\n"
    with open("sala.txt", "w", encoding="utf-8") as file:
        file.write(data)

# Utilizando Json para abrir um ficheiro e salvar informações nele
if False:
    clubs : dict = {
        "teams" : {
            "SEP" : "Sociedade Esportiva Palmeiras",
            "SLB" : "Sport Lisboa e Benfica",
            "SCP" : "Sporting Clube de Portugal",
            "FCP" : "Futebol Clube do Porto",
        }
    }

    import json
    from json import dump, load
    import os

    if os.path.exists("clubs.json"):
        f = open("clubs.json","r")
        clubs_2 = json.load(f)
        f.close()

    with open("clubs.json", "w") as filename:
        # json.dump(clubs, filename)
        clubs["score"] = "1-0"
        dump(clubs, filename, indent=2)
        
    clubs_2 = dict()
    with open("clubs.json", "r") as filename:
        clubs_2 = json.load(filename)
        print(clubs_2["teams"]["SEP"])

if False:
    import os
    
    basepath = r"C:\Users\Thiago Yabuki\Documents\IPCA\Segundo Ano\Segundo Semestre\Processamento de Linguagens\Aulas"
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)) and entry.endswith(".py"):
            print(entry)