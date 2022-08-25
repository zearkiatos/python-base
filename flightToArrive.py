def convert_minutes_to_seconds(minutes: int) -> int:
    return (minutes*3600)/60


def convert_hours_to_seconds(hours: int) -> int:
    return (hours*86400)/24


def arrive_flight_calculator(leaveHours: int, leaveMinutes: int, leaveSeconds: int, durationHours: int, durationMinutes: int, durationSeconds: int) -> str:
    total_seconds = leaveSeconds + durationSeconds
    aditional_minutes = 0
    if(total_seconds >= 60):
        ss = total_seconds - 60
        aditional_minutes += 1
    else:
        ss = total_seconds

    total_minutes = leaveMinutes + durationMinutes + aditional_minutes
    aditional_hours = 0
    if(total_minutes >= 60):
        mm = total_minutes - 60
        aditional_hours += 1
    else:
        mm = total_minutes

    total_hours = leaveHours + durationHours + aditional_hours
    if(total_hours >= 24):
        hh = total_hours - 24
        aditional_hours += 1
    else:
        hh = total_hours

    return str(hh).zfill(2)+":"+str(mm).zfill(2)+":"+str(ss).zfill(2)


def calculate_arrive_flight(flights: list) -> list:
    arrive_flight = []
    for flight in flights:
        leave_time = flight['leave_time'].split(':')
        duration_time = flight['duration_time'].split(':')
        time = arrive_flight_calculator(int(leave_time[0]), int(leave_time[1]), int(
            leave_time[2]), int(duration_time[0]), int(duration_time[1]), int(duration_time[2]))
        arrive_flight.append({
            'id': flight['id'],
            'arrive_time': time
        })
    return arrive_flight

def latest_flight(flights: list)->dict:
    latest = flights[0]
    print(flights)
    for flight in flights:
        first_time = flight['arrive_time'].split(':')
        first_hh = int(first_time[0])
        first_mm = int(first_time[1])
        first_ss = int(first_time[2])
        latest_time = latest['arrive_time'].split(':')
        latest_hh = int(latest_time[0])
        latest_mm = int(latest_time[1])
        latest_ss = int(latest_time[2])
        if (first_hh > latest_hh):
            latest = flight
        if ( first_hh >= latest_hh and first_mm > latest_hh):
            latest = flight
        if ( first_hh >= latest_hh and first_mm >= latest_mm and first_ss > latest_ss):
            latest = flights
    
    return latest


flights = [{
    "id": 1,
    "leave_time": '11:48:10',
    "duration_time": '2:11:58'
},
    {
    "id": 2,
    "leave_time": '07:59:10',
    "duration_time": '2:10:00'
}]

flights_arrive = calculate_arrive_flight(flights)

print(latest_flight(flights_arrive))
