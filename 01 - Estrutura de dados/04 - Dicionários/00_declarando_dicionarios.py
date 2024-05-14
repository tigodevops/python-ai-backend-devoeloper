## Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas
## em uma dada instância do diciónario

#Exemplo 1 

pessoa = {"nome": "Thiago", "idade": 28}
print(pessoa)
#Exemplo 2 utilizando a classe dict

pessoa = dict(nome="Thiago", idade=28)
print(pessoa)

# Exemplo 3 pegando um dicionário já montato e acrescentando uma nova chave:valor
pessoa["telefone"] = "3333-3333"
print(pessoa)

