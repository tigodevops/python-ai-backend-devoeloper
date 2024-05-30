## Importando
## import datetime

## Importando de outra maneira
from datetime import date
from datetime import datetime
from datetime import time

## Colocando em uma variavel
data = date(2023, 7, 10)
print(data)

## Pegando dia mes e ano atual
print(date.today())

data_hora = datetime(2023, 7, 10, 21, 10, 10)
print(data_hora)
print(datetime.today())

hora = time(10, 20, 3)
