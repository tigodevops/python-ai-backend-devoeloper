# Operadores de Identidade #

# São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição de memória.


curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

exp = curso is nome_curso

exp_2 = curso is not nome_curso

exp_3= saldo is limite 

print(exp)
print(exp_2)
print(exp_3)

saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)


