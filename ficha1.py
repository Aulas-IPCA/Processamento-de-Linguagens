import pandas as pd

notas_UCS = {
    "Física": 12,
    "Programação Orientada a Objetos": 18,
    "Projeto de Engenharia de Software": 15
}

media = sum(notas_UCS.values()) / len(notas_UCS)

print(f"Média das notas do último semestre: {media}")

with open("Notas_Semestre_Passado.txt", "w") as file:
    for disciplina, nota in notas_UCS.items():
        file.write(f"{disciplina}: {nota}\n")

# Lê ficheiro txt
notas_UCS_lidas = {}
with open("notas_semestre_passado.txt", "r") as file:
    for line in file:
        disciplina, nota = line.strip().split(": ")
        notas_UCS_lidas[disciplina] = int(nota)

# Converter para DataFrame e exporta para Excel
df = pd.DataFrame(list(notas_UCS_lidas.items()), columns=["Disciplina", "Nota"])
df.to_excel("notas_semestre_passado.xlsx", index=False)

carros = {
    "Toyota": ["Corolla", "Camry", "Rav4"],
    "Honda": ["Civic", "Accord", "CR-V"],
    "Ford": ["Mustang", "Fusion", "Escape"],
    "Chevrolet": ["Camaro", "Malibu", "Equinox"],
    "BMW": ["3 Series", "5 Series", "X5"]
}

carros_com_ano = {marca: [(modelo, 2020) for modelo in modelos] for marca, modelos in carros.items()}
