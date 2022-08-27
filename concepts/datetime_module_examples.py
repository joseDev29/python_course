import datetime

# datetime.time(hour?, minutes?, seconds?)
my_hour = datetime.time(16, 34, 45)
print(my_hour)
print(type(my_hour))
print(my_hour.hour)
print(my_hour.second)
print(my_hour)

# datetime.date(year, month, day)
my_date = datetime.date(2020, 9, 20)
print(my_date)
print(my_date.day)
print(my_date.month)
print(my_date.today())

# datetime.datetime(year, month, day, hour?, minutes?, seconds?)
my_datetime = datetime.datetime(2005, 5, 23, 18, 45, 57)
print(my_datetime)
print(my_datetime.day)
print(my_datetime.minute)

print(datetime.datetime(2020, 7, 23))

print(my_datetime.today())

# replace return new date with new params info
print(my_datetime.replace(month=11))

birth = datetime.datetime(1940, 3, 23)
death = datetime.datetime(2080, 4, 26)
life = death - birth
print(life)
print(life.days)
print(round(life.days / 365, 2))

wake_up = datetime.datetime(2020, 9, 13, 6, 20)
slept = datetime.datetime(2020, 9, 20, 18, 20)
print(round((wake_up - slept).seconds / (60 * 60), 2))  # out: hours
