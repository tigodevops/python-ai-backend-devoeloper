class animal():
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join({f'{chave}-{valor}' for chave, valor in self.__dict__.items()})}"


class ave(animal):
    def __init__(self, nro_patas):        
        super().__init__(nro_patas)

class mamifero(animal):
    def __init__(self, nro_patas, cor_pelo):
        self.cor_pelo = cor_pelo        
        super().__init__(nro_patas)

class Cachorro(mamifero):
    def __init__(self, nro_patas, cor_pelo):
        self.nro_patas=nro_patas
        self.cor_pelo = cor_pelo
        

class Gato(mamifero):
    def __init__(self, nro_patas, cor_pelo):
        self.nro_patas = nro_patas
        self.cor_pelo = cor_pelo        

class Leao(mamifero):
    def __init__(self, nro_patas, cor_pelo):
        self.nro_patas = nro_patas
        self.cor_pelo = cor_pelo

class Ornitorrinco(mamifero):
    def __init__(self, nro_patas, cor_pelo):
        self.nro_patas = nro_patas
        self.cor_pelo = cor_pelo


gato = Gato(4, "preto")
print(gato)

ornitorrinco = Ornitorrinco (4, "Branco")
print(ornitorrinco)
