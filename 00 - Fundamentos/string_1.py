
## Manipulando String com Python! ##

# Strip removendo espaços em branco
nome = "thiago"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "   olá mundo "

print(texto)
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

# Centralizando

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, '#'))

# Junção
print("P-y-t-h-o-n")
print("-".join(menu))

for letra in menu:
    print(letra, end='-')
