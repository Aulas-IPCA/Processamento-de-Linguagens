import ply.lex as lex

text: str = "Hoje é dia 11 de abril de 2024."
tokens = ("NUM",)
result : int = 0
numbers : list = []

def t_NUM(t):   # token: NUM
    r"[0-9]+"
    # t.value   # lexema: valor do token

    global result
    result += int(t.value)

    global numbers
    numbers.append(int(t.value))

def t_error(t):
    print(f"Invalid character: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
lexer.input(text)

for token in lexer:
    pass

print(f"Números encontrados: {numbers}")
print(f"Soma total: {result}")