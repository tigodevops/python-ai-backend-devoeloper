# Adição
print(1 + 1)

# Subtração
print(10 - 2)

#Multiplicação
print(4 * 3)

#Divisão
print(12 / 3)

#Divisão Inteira
print(12 // 3 )

#Módulo
print(10 % 3)

#Exponenciação
print (2 ** 3)


# Precedência dos Operadores #
# A definição indica a seguinte ordem como a correta:
# Parênteses
# Expoêntes
# Multiplicações e divisões (da esquerda para a direita)
# Somas e subtrações (da esquerda para a direita)

# Exemplos

print(10 - 5 * 2)
print((10 - 5) * 2)
print(10 ** 2 * 2)
print(10 ** (2 * 2))
print(10 / 2 * 4)

produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

# Forçando a precedência

x = (10 + 5) * 4
y = (10 / 2) + (25 * 2) - (2 ** 5)
z = 10 / 2 + 25 * 2 - 2 ** 5
a = y = (10 / 2) + ((25 * 2) - (2 ** 5))

print(x)
print(y)
print(z)
print(a)
