carros = ["gol", "HB20", "palio"]
print(carros)

## Percorrendo a lista !##

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")