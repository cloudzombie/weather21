#!/usr/bin/env python3

# Import methods from the 21 Bitcoin Library
from two1.commands.config import Config
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

SERVER_IP_ADDRESS='10.244.132.211'
SERVER_PORT='5050'

MODE_LIST= ['current', 'forecast']

# Configure your Bitcoin wallet.
username = Config().username
wallet = Wallet()
requests = BitTransferRequests(wallet, username)

# Send city name, country code, unit and language to the endpoint
def send_city(mode, cityname, countrycode, unit, language):
    # Display info the user is sending
    print('Mode: {0}'.format(mode))
    print('City: {0}'.format(cityname))
    print('Country: {0}'.format(countrycode))
    print('Unit: {0}'.format(unit))
    print('Language: {0}'.format(language))

    # 402-payable endpoint URL and request
    if mode == MODE_LIST[0]:
        route_url = '/weather/current/'
    else:
        route_url = '/weather/forecast/'

    if countrycode:
       weather_url = 'http://' + SERVER_IP_ADDRESS + ':' + SERVER_PORT + route_url + 'city?cityname={0}&countrycode={1}'
    else:
       weather_url = 'http://' + SERVER_IP_ADDRESS + ':' + SERVER_PORT + route_url + 'city?cityname={0}'

    if unit:
       weather_url = weather_url + '&unit={2}'

    if language:
       weather_url = weather_url + '&lang={3}'

    response = requests.get(url=weather_url.format(cityname, countrycode, unit, language))

    print('URL: ' + response.url)

    print(response.text)

# Send zip code, country code, unit and language to the endpoint
def send_zip(mode, zipcode, countrycode, unit, language):
    # tell the user what info they're sending
    print('Mode: {0}'.format(mode))
    print('Zip: {0}'.format(zipcode))
    print('Country: {0}'.format(countrycode))
    print('Unit: {0}'.format(unit))
    print('Language: {0}'.format(language))

    # 402-payable endpoint URL and request
    if mode == MODE_LIST[0]:
        route_url = '/weather/current/'
    else:
        route_url = '/weather/forecast/'

    weather_url = 'http://' + SERVER_IP_ADDRESS + ':' + SERVER_PORT + route_url + 'zip?zipcode={0}&countrycode={1}'

    if unit:
       weather_url = weather_url + '&unit={2}'

    if language:
       weather_url = weather_url + '&lang={3}'

    response = requests.get(url=weather_url.format(zipcode, countrycode, unit, language))

    print('URL: ' + response.url)

    print(response.text)

# Send latitude, longitude, unit and language to the endpoint
def send_geo(mode, latitude, longitude, unit, language):
    # tell the user what info they're sending
    print('Mode: {0}'.format(mode))
    print('Latitude: {0}'.format(latitude))
    print('Longitude: {0}'.format(longitude))
    print('Unit: {0}'.format(unit))
    print('Language: {0}'.format(language))

    # 402-payable endpoint URL and request
    if mode == MODE_LIST[0]:
        route_url = '/weather/current/'
    else:
        route_url = '/weather/forecast/'

    weather_url = 'http://' + SERVER_IP_ADDRESS + ':' + SERVER_PORT + route_url + 'geo?latitude={0}&longitude={1}'

    if unit:
       weather_url = weather_url + '&unit={2}'

    if language:
       weather_url = weather_url + '&lang={3}'

    response = requests.get(url=weather_url.format(latitude, longitude, unit, language))

    print('URL: ' + response.url)

    print(response.text)

# Read args from command line.
# send_city():
# python3 weather.py "current" "London" "uk" "" ""
# python3 weather.py "current" "London" "uk" "metric" "fr"
# python3 weather.py "forecast" "London" "uk" "" ""
# python3 weather.py "forecast" "London" "uk" "metric" "fr"
# send_zip():
# python3 weather.py "current" "94040" "us" "imperial" "es"
# python3 weather.py "forecast" "94040" "us" "imperial" "es"
# seng_geo():
# python3 weather.py "current" "51.51" "-0.13" "" ""
# python3 weather.py "forecast" "51.51" "-0.13" "" ""
if __name__ == '__main__':
    from sys import argv
    send_city(argv[1], argv[2], argv[3], argv[4], argv[5])
    #send_zip(argv[1], argv[2], argv[3], argv[4], argv[5])
    #send_geo(argv[1], argv[2], argv[3], argv[4], argv[5])
