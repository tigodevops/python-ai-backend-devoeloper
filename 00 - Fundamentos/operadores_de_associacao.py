# Operadores de associação #

# São operadores utilizado para verificar se um objeto está presente em uma sequencia

curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

exp = "Python" in curso

exp_1 = "maça" not in frutas

exp_2 = 200 in saques

print(exp)
print(exp_1)
print(exp_2)