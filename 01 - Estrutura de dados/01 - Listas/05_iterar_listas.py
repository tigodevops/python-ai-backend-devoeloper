carros = str(input("inform seu carro : "))
print(carros)

## Percorrendo a lista !##

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")