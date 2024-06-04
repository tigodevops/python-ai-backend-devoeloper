import textwrap

def menu(): 
    menu = """

    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo usuário
    [5]\tNova Conta
    [6]\tListar conta
    [0]\tSair
     
    => """

    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato):
    if valor > 0:            
         saldo += valor
         extrato += f"Depósito: R$ {valor:.2f}\n" 
         print("\n!!! Depósito realizado com sucesso !!!")
    else:
        print("\n@@@ Operção falhou! O valor informado inválido. @@@")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
            print("Saque não realizado! Você não tem saldo suficiente para saque!")

    elif excedeu_limite:
            print("Saque não realizado! o valor do saque excedeu o limite!")

    elif excedeu_saques:
            print("Saque não realizado! Você excedeu o limite de saques para hoje!")

    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
            print("\n!!! Saque realizado com sucesso !!!")

    else:
        print("\n@@@ Operção falhou! O valor informado inválido. @@@") 

    return saldo, extrato

def exibir_extrato(saldo, /,  extrato):
     print("======================EXTRATO==========================")
     print("Não foram realizadas transações." if not extrato else extrato)
     print(f"\nsaldo: R$ {saldo:.2f}")
     print("=======================================================")
     
def criar_usuario(usuarios):
    cpf = input("Informe o CPF: (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
         print("\n@@@ Já existe usuário com esse CPF! @@@")
         return


    nome = input("Informe seu nome completo: ")
    dt_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa):")
    endereco = input("informe seu endereço: (logradouro, nro - bairro - cidade/sigla estado)")

    usuarios.append({"nome": nome, "dt_nascimento": dt_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuario criado com sucesso!")
    
def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None
          
def criar_conta(agencia, numero_conta, usuarios):
     cpf = input("Informe o cpf do usuario: ")
     usuarios = filtrar_usuario(cpf, usuarios)

     if usuarios:
          print("Conta criada com sucesso! ")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuarios}
     
     print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado  @@@")

def listar_contas(contas):
     for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}


        """
        print("=" * 100)
        print(textwrap.dedent(linha))
              
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor, 
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                )
            
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                 contas.append(conta)

        elif opcao == "6":
             listar_contas(contas)

        elif opcao == "q":
             break

main()