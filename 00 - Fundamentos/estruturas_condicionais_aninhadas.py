# IF aninhado #
conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 2000
cheque_especial = 450



if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado utilizando cheque especial")
    else:
        print("Não possível ralizar o saque, saldo insuficiente")
elif  conta_universitaria:
    if saque <= saldo:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente para saque")

elif conta_especial:
    print("Conta especial selecionada.")
    
else:
    print("Sistema não reconheceu seu tipo de conta, por favor entrar em contato com o seu gerente.")
