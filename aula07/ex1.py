import ply.lex as lex

text : str = "Hoje é dia 12-04-2024, e também 12-04-24, o nosso teste estava marcado para dia 23/05/2024 " \
                "e agora ficou para dia 7\\06\\2024." \
                "E essa data esta errada 12-04-202."

tokens : set = ("DATE1", "DATE2", "DATE3")

counter : int = 0

def t_DATE1(t):
    r"\d{1,2}[\\\-\/]\d{1,2}[\\\-\/](\d{4}|\d{3}|\d{2})"
    
    global counter
    counter = counter + 1

    # import re
    # regex = "-"
    # simbols = re.findall(regex, t.value)
    # idx = t.value.index(simbols[0])
    # sub_string = t.value[idx+1:]

    if "-" in t.value:
        numbers : list = t.value.split("-")
        if len(numbers[2]) == 3:
            print(f"Ano {numbers[2]} invalido")
    elif "\\" in t.value:
        numbers : list = t.value.split("\\")
        if len(numbers[2]) == 3:
            print(f"Ano {numbers[2]} invalido")
    elif "\/" in t.value:
        numbers : list = t.value.split("\/")
        if len(numbers[2]) == 3:
            print(f"Ano {numbers[2]} invalido")

    print(f"Data encontrada: {t.value}")

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()
lexer.input(text)

for token in lexer:
    pass

print(f"Total de datas encontradas: {counter}")