### Fechas ###

import datetime #con esto estamos importando el modulo datetime

#con esto traemos la fecha y hora actual en formato (2024-06-14 18:54:20.919159)
now = datetime.datetime.now()
print(now)



#De esta manera puedo acceder a las diferentes atributos del modulo datetime
from datetime import datetime
from datetime import timedelta
from datetime import time
from datetime import date




min = datetime.min
print(min)

now_= datetime.now()
print(now_.second)
print(now_.minute)
print(now_.hour)
print(now_.day)
print(now_.month)
print(now_.year)

#el timestamp es un formato q indica el número de segundos transcurridos desde una fecha y hora o época específicas.
# Cuenta los segundos desde la medianoche del 1 de enero de 1970 (época).
print(now_.timestamp())


year_2024 = datetime(2024,5,1)

def now__(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    
     

now__(now)
print(year_2024)



# Time
current_time = time(22,4,1)
print(current_time)


current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)



# Date
current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)

print(current_date.month)



# Operaciones con fechas
diff = year_2024 - now
print(diff)

diff = year_2024.date() - current_date
print(diff)




# Timedelta
start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
