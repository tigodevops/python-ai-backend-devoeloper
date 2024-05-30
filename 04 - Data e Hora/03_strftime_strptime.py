from datetime import datetime

d = datetime.now()

#formatando
print(d.strftime("%d/%m/%Y %H:%M"))

#Convertento string para datetime

date_string = "20-07-2023 15:30"
d = datetime.strptime(date_string, "%d-%m-%Y %H:%M")
print(d)

data_hora_atual = datetime.now()
data_hora_str = "26-05-2024 08:53"
mascara_ptbr = "%d-%m-%Y %H:%M:%S"
mascara_str = "%d-%m-%Y %H:%M"

data_hora_atual = datetime.strftime(data_hora_atual, mascara_ptbr)
print(data_hora_atual)

#data_hora_str = datetime.strptime(data_hora_str, mascara_str)
#print(type(data_hora_str))

data_convertida = datetime.strptime(data_hora_str, mascara_str)
print(type(data_convertida))
print(data_convertida.strftime("%Y"))
