menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
 

=> """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_valor = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numeros_saques > LIMITE_SAQUES

        if excedeu_valor:
            print("Saque não realizado! Você não tem saldo suficiente para saque!")

        elif excedeu_limite:
            print("Saque não realizado! o valor do saque excedeu o limite!")

        elif excedeu_saques:
            print("Saque não realizado! Você excedeu o limite de saques para hoje!")

        elif valor > 0:            
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numeros_saques += 1

           
        else:
            print("Operação falhou! O valor informado é inválido!")
         
     
    elif opcao == "3":
        print("\n ================ EXTRATO =================")
        print("Não foram realizadas transações." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print(f"\nlimite: R$ {limite:.2f}")
        print("================================================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    

