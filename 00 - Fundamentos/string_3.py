## Fatiamento de string técnica utilizada para tetornar partes de ima string ##

nome = "Thiago Eulalio Reimberg borba"

#Retornando a primeira letra da string
print(nome[0])

#Retornando do inicio da string até o caractere 9(nesse caso eu passo o fim indice 9 e ele retorna do começo)
print(nome[:9])

#Retornado a partir do caractere 10 que indiquei como inicio
print(nome[10:])

#Retornando do caractere iniciado no 10 até o 16
print(nome[10:16])

#Retornando do caractere 10 ao 16 , mas recuperando de 2 em 2 caractere
print(nome[10:16:2])

#Retorna uma cópia da string
print(nome[:])

# Retorna o espelho da string
print(nome[::-1])

#Retorna pegando a ultima letra da string
print(nome[-1])