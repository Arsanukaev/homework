from datetime import date, datetime, timedelta
delta1 = timedelta(days = 1)
delta2 = timedelta(weeks = 4)
today = date.today()
monthago = today - delta2
yesterday = today - delta1
date_string = "01/01/17 12:10:03.234567"
dt = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
print(today)
print(monthago)
print(yesterday)
print(dt)