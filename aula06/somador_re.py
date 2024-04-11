import re

text: str = "Hoje é dia 11 de abril de 2024."
regex = r'\d+'

number : list = re.findall(regex, text)

number = [int (number) for number in number]

result : int = sum(number)

print(f"O resultado da soma dos números é: {number}")
print(f"Soma total: {result}")


