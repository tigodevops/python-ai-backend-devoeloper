class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando Motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join({f'{chave}-{valor}' for chave, valor in self.__dict__.items()
})}"
 
class motocicleta(veiculo):
    pass

class carro(veiculo):
    pass

class caminhao(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado


    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = motocicleta("preta", "ABD-1237", 2)
#moto.ligar_motor()#

carro = carro("branco", "XPT-1237", 4)
#carro.ligar_motor()#
caminhao = caminhao("roxo", "GDB-1237", 8, False)
#caminhao.ligar_motor()
#caminhao.esta_carregado()

print(moto)
print(carro)
print(caminhao)