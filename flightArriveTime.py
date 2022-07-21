def convertMinutesToSeconds(minutes:int)->int:
    return (minutes*3600)/60

def convertHoursToSeconds(hours:int)->int:
    return (hours*86400)/24

def arriveFlightCalculator(leaveHours:int, leaveMinutes:int, leaveSeconds:int, durationHours:int,durationMinutes:int, durationSeconds:int)->str:
    hoursInSeconds = convertHoursToSeconds(leaveHours) + convertHoursToSeconds(durationHours)
    minutesInSeconds = convertMinutesToSeconds(leaveMinutes) + convertMinutesToSeconds(durationMinutes)
    hours = (hoursInSeconds*24)/86400
    fullHours = int(hours)
    if fullHours >= 24:
        hh = fullHours - 24
    else:
        hh = fullHours

    minutes = (minutesInSeconds*60)/3600
    fullMinutes = int(minutes)

    if fullMinutes >= 60:
        mm = fullMinutes - 60
        if hh == 23:
            hh=0
        else:
            hh+=1
    else:
        mm = fullMinutes
    
    seconds = leaveSeconds + durationSeconds
    if seconds >= 60:
        ss = seconds - 60
        if mm == 60:
            mm = 0
        else:
            mm+=1
    else:
        ss = seconds
    
    return str(hh)+":"+str(mm)+":"+str(ss)

print(arriveFlightCalculator(23,30,0,8,40,20))