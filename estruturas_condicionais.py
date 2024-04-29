# Estruturas Condicionais #
# Permite o desvio de fluxo de controle, quando determinadas expressões lógica são atendidas.

# Exemplo realizando Saque com if

def sacando(valor):
    saldo = 2000.0
    saque =  float(input("Informe o valor do saque: "))

    if saldo >= saque:
        print("Realizando saque!")

    if saldo < saque:
            print("Saldo insuficiente")

sacando(1)


# Exemplo realizando saque com if / else

def sacando2(valor):
    saldo = 2000.0
    saque = float(input("Qual o valor do saque: "))

    if saldo >= saque:
        print("Realizando saque")
    else:
        print("Saldo insuficiente")

sacando2(1)

# Exemplo sacando com if / else / elif

opcao = int (input("Informe uma opção: [1] Sacar \n[2] Extrato: "))
if opcao == 1:
     print("Qual o valor para Saque")
elif opcao == 2:
     print("Extrato")
else:
     print("Opção inválida")

# Idade += 18#

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade:"))
if idade >= 18:
     print("Pode tirar habilitação")
if idade <18:
     print("Não pode tirar a habilitação")


idade = int(input("Informe sua idade:"))
if idade >= 18:
     print("pode tirar habilitação")
else:
     print("Não pode tirar habilitação")

if idade >= MAIOR_IDADE:
     print("Pode tirar habilitação")
elif idade >= IDADE_ESPECIAL:
     print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas")
else: print("Ainda não pode tirar a habilitação")
