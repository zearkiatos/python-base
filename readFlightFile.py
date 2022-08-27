def upload_flights(file_path: str) -> dict:
    flights = {}
    file = open(file_path)
    titles = file.readline().split(",")
    print(titles)
    line = file.readline()
    while len(line) > 0:
        data = line.split(",")
        flight_code = data[1]
        flight = {}
        flight["airline"] = data[0]
        flight["origin"] = data[2]
        flight["destiny"] = data[3]
        flight["distance"] = data[4]
        flight["leave"] = data[5]
        flight["duration"] = data[6]
        flight["delay"] = data[7]
        flights[flight_code] = flight
        line = file.readline()
    file.close()
    return flights


print(upload_flights('flight_airline.csv'))
