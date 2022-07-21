def convertMinutesToSeconds(minutes:int)->int:
    return minutes*60

def convertHoursToSeconds(hours:int)->int:
    return hours*3600

def arriveFlightCalculator(leaveHours:int, leaveMinutes:int, leaveSeconds:int, durationHours:int,durationMinutes:int, durationSeconds:int)->str:
    totalSeconds = leaveSeconds + durationSeconds + convertMinutesToSeconds(leaveMinutes) + convertMinutesToSeconds(durationMinutes) + convertHoursToSeconds(leaveHours) + convertHoursToSeconds(durationHours)
    print(totalSeconds)
    hours = totalSeconds/3600
    fullHours = totalSeconds//3600
    decimalHours = hours - fullHours
    minutes = decimalHours*60
    fullMinutes = int(minutes)
    decimalMinutes = minutes - fullMinutes
    seconds = decimalMinutes*60
    fullSeconds = int(seconds)
    

    return str(fullHours)+":"+str(fullMinutes)+":"+str(fullSeconds)

print(arriveFlightCalculator(23,30,0,8,40,20))