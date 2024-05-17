def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire seu dinheiro na boca do caixa.")

    print("Seu saldo é insuficiente para saque, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor
    
sacar(1000)
depositar(700)