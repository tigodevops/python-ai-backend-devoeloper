# pip install pytz

import pytz
from datetime import datetime

data = datetime.now(pytz.timezone("Europe/Oslo"))
data_2 = datetime.now(pytz.timezone("America/Sao_Paulo"))
print(data)
print(data_2)