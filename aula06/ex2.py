# Evolua o seu processador no sentido de escrever a soma (parcial) sempre que encontre uma palavra igual.
import re

text: str = "Hoje é dia 11 de abril de 2024. Isto é = a dizer que hoje é 11=04=2024."
regex = r'='
eq : list = re.findall(regex, text)

text_cpy : str = text
result_parcial : int = 0

for e in eq:
    idx = text_cpy.index("=")

    regex = r'\d+'
    numbers : list = re.findall(regex, text_cpy[:idx])
    numbers = [int (number) for number in numbers]

    print(f"Soma parcial: {(sum(numbers)+result_parcial)}")

    result_parcial += sum(numbers)
    text_cpy = text_cpy[idx+1:]

regex = r'\d+'
numbers : list = re.findall(regex, text)
numbers = [int(number) for number in numbers]
result : int = sum(numbers)

print(f"Numeros encontrados: {numbers}")
print(f"Soma total: {result}")