import math
    
def get_station_data(filename: str):
    stations = {}
    with open(filename) as new_file:
        for lines in new_file:
            info = lines.split(";")
            if info[0] == "Longitude":
                continue
            name = info[3]
            stations[name] = float(info[0]), float(info[1])
    return stations
    
def distance(stations: dict, station1: str, station2: str):
    
    if station1 and station2 in stations:
        longitude1 = stations[station1][0]
        longitude2 = stations[station2][0]
        latitude1 = stations[station1][1]
        latitude2 = stations[station2][1]
        x_km = (longitude1 - longitude2) * 55.26
        y_km = (latitude1 - latitude2) * 111.2
        distance_km = math.sqrt(x_km**2 + y_km**2)
    
    return distance_km
    
def greatest_distance(stations: dict):
    greatest = 0
    complete = ()
    for station1 in stations:
        for station2 in stations:
            longitude1 = stations[station1][0]
            longitude2 = stations[station2][0]
            latitude1 = stations[station1][1]
            latitude2 = stations[station2][1]
            x_km = (longitude1 - longitude2) * 55.26
            y_km = (latitude1 - latitude2) * 111.2
            distance_km = math.sqrt(x_km**2 + y_km**2)
            if distance_km > greatest:
                greatest = distance_km
                complete = station1, station2, greatest
    return complete
    
if __name__ == "__main__":
    stations = get_station_data("stations1.csv")
    print(distance(stations, "Designmuseo", "Hietalahdentori"))         
    print(greatest_distance(stations))