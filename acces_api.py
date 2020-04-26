import requests


def get_stations(json, city_keyword):
    return [station for station in json if city_keyword in station['longname']]


def get_station_status(station):
    water_value = station['timeseries'][0]['currentMeasurement']['value']
    trend = station['timeseries'][0]['currentMeasurement']['trend']
    return water_value, trend

if __name__ == '__main__':
    url = 'https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations.json?includeTimeseries=true' \
          '&includeCurrentMeasurement=true'
    # here I could hard-code the four shortnames for the spots (PASSAU ILZSTADT, PASSAU DONAU, PASSAU LUITPOLDBRÜCKE DFH,
    # PASSAU STEINBACHBRÜCKE DFH). But instead I chose a more general approach that looks for PASSAU generally
    city = 'PASSAU'
    stations_json = requests.get(url).json()
    stations = get_stations(stations_json, city)
    for station in stations:
        print(station['longname'])
        water_level, trend = get_station_status(station)
        print(f'level: {water_level}')
        print(f'trend: {trend}')

