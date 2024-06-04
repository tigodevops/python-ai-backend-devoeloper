def recomendar_plano(consumo):          

    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"

    elif consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"

    else:
        return "Plano Premium Fibra - 300Mbps"


print("Informe o seu consumo médio mensal de dados em Gb? ")

consumo = float(input())
print(recomendar_plano(consumo))



