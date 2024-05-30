def mensagem(nome):
    print("executando nome")
    return f"oi {nome}"

def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Olá tudo bem com você {nome} ?"

def executar(funcao):
    print("executando executar")
    return funcao("Guilherme")


print(executar(mensagem))
print(executar(mensagem_longa))