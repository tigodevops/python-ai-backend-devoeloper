# Exemplo sem repetição para entendimento #

numero = int(input("Informe o numero:"))
print(f"{numero}")

numero += 1
print(numero)

numero += 1
print(numero)

# Comando for e a função built-in range #
texto = input("Inform um texto:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() 

# For com built-in #
# num = int(input("Informe dois numeros, separados por virgula: "))

for numero in range (10):
    print(numero, end=" ")

# Exibindo a tabuada do 5 com built-in range#

for numero in range (0, 51, 5):
    print (numero, end=" ")

