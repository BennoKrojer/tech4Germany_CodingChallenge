import requests
import config
import display


def get_stations(json, city_keyword):
    # here I could hard-code the four shortnames for the spots (PASSAU ILZSTADT, PASSAU DONAU, PASSAU LUITPOLDBRÜCKE
    # DFH, PASSAU STEINBACHBRÜCKE DFH). But instead I chose a more general approach that looks for PASSAU generally
    return [station for station in json if city_keyword in station['longname']]


def get_station_status(station):
    water_value = station['timeseries'][0]['currentMeasurement']['value']
    trend = station['timeseries'][0]['currentMeasurement']['trend']
    return water_value, trend


def get_city_status(url, city):
    stations_json = requests.get(url).json()
    stations = get_stations(stations_json, city)
    result = []
    for station in stations:
        water_level, trend = get_station_status(station)
        city_info = {'station': station['longname'],
                     'level': water_level,
                     'trend': display.emojify(config.trends[trend]),
                     'warnings': display.emojify(display.get_warnings(water_level))}
        result.append(city_info)
    return result
