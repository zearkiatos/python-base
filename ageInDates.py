def calculateAge(birthday:int, birthmonth:int, birthyear:int,currentday:int, currentmonth:int,currentyear:int)->str:
    days = birthday + currentday
    month = currentmonth
    year = currentyear - birthyear
    return str(year)+','+str(month)+','+str(days)

print(calculateAge(5,8,2019,15,8,2019))

