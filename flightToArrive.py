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
        arrive_flight.append([{
            'id': flight['id'],
            'arrive_time': time
        }])
    return arrive_flight


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


print(calculate_arrive_flight(flights))
