def meu_decorador(funcao):
    def envelope():
        print("Faz algo altens da função")
        funcao()
        print("Faz algom depois da função")

    return envelope

def ola_mundo():
    print("Olá Mundo")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()