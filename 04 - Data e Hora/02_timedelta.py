# Criando data e hora
from datetime import time, date, datetime, timedelta


d = datetime(2023, 7, 1, 13, 45)
print(d)

#Adicionando uma semana
d = d + timedelta(weeks=1)
print(d)

tipo_carro = 'G' # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O Carro chegou: {data_atual} e ficará pronto às {data_estimada}')
elif tipo_carro =="M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O Carro chegou: {data_atual} e ficará pronto às {data_estimada}')
else:
   data_estimada = data_atual + timedelta(minutes=tempo_grande)
   print(f'O Carro chegou: {data_atual} e ficará pronto às {data_estimada}')

   print (date.today() - timedelta(days=1))

resultado = datetime(2023, 7, 25, 15, 19, 20) -timedelta(hours=1) #trabalhando somente com hh-mm-ss
print(resultado.time())

print(datetime.now().date())