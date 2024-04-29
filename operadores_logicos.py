# Operadores Lógicos #
# São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão çógica.
# Quando um operador de comparação é utilizado, o resultado retornado é um booleano

#op_comparacao + op_logico + op_comparacao n....

saldo = 1000
saque = 200
limite = 100
conta_especial = True

saldo >= saque
print(saldo)

saldo >= saque and saque >= limite
print(saldo)

saldo >= saque or saque >= limite
print(saldo)

## Operador de negação

# contatos_emergencia []

not 1000 > 1500

# not contatos_emergencia

not "saque 1500;"

not ""

# Parênteses - Precedência

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

# AND =  para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

print(True and True)
print(True and False)
print(True or True)
print(False and False)
print(False or False)
print(False or True)

print(exp)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 =  conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)





