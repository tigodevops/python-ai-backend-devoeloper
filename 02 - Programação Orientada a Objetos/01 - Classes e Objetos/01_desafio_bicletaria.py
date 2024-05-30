class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plin Plin ...")

    def parar(self):
        print("Parar bicleta!")
        print("Bicicleta parada!")

    def __str__(self):
        return f"{self.__class__.__name__}: {', ' .join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("Branca", "Caloi", "1999", "600")
print(b1)

