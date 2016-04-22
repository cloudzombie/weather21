#!/usr/bin/env python3

# Import methods from the 21 Bitcoin Library
from two1.commands.config import Config
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

SERVER_IP_ADDRESS='10.244.132.211'
SERVER_PORT='5050'

# Configure your Bitcoin wallet. 
username = Config().username
wallet = Wallet()
requests = BitTransferRequests(wallet, username)

# Send city name, country code, unit and language to the endpoint
def send_city(cityname, countrycode, unit, language):
    # Display info the user is sending
    print('City: {0}'.format(cityname))
    print('Country: {0}'.format(countrycode))
    print('Unit: {0}'.format(unit))
    print('Language: {0}'.format(language))

    # 402-payable endpoint URL and request
    if countrycode:
       weather_url = 'http://' + SERVER_IP_ADDRESS + ':' + SERVER_PORT + '/weather/city?cityname={0}&countrycode={1}'
    else:
       weather_url = 'http://' + SERVER_IP_ADDRESS + ':' + SERVER_PORT + '/weather/city?cityname={0}'

    if unit:
       weather_url = weather_url + '&unit={2}'
    
    if language:
       weather_url = weather_url + '&lang={3}'
    
    response = requests.get(url=weather_url.format(cityname, countrycode, unit, language))

    print('URL: ' + response.url)

    print(response.text)

# Send zip code, country code, unit and language to the endpoint
def send_zip(zipcode, countrycode, unit, language):
    # tell the user what info they're sending
    print('Zip: {0}'.format(zipcode))
    print('Country: {0}'.format(countrycode))
    print('Unit: {0}'.format(unit))
    print('Language: {0}'.format(language))

    # 402-payable endpoint URL and request
    weather_url = 'http://' + SERVER_IP_ADDRESS + ':' + SERVER_PORT + '/weather/zip?zipcode={0}&countrycode={1}'

    if unit:
       weather_url = weather_url + '&unit={2}'
    
    if language:
       weather_url = weather_url + '&lang={3}'
    
    response = requests.get(url=weather_url.format(zipcode, countrycode, unit, language))

    print('URL: ' + response.url)

    print(response.text)

# Send latitude, longitude, unit and language to the endpoint
def send_geo(latitude, longitude, unit, language):
    # tell the user what info they're sending
    print('Latitude: {0}'.format(latitude))
    print('Longitude: {0}'.format(longitude))
    print('Unit: {0}'.format(unit))
    print('Language: {0}'.format(language))

    # 402-payable endpoint URL and request
    weather_url = 'http://' + SERVER_IP_ADDRESS + ':' + SERVER_PORT + '/weather/geo?latitude={0}&longitude={1}'

    if unit:
       weather_url = weather_url + '&unit={2}'
    
    if language:
       weather_url = weather_url + '&lang={3}'
    
    response = requests.get(url=weather_url.format(latitude, longitude, unit, language))

    print('URL: ' + response.url)

    print(response.text)

# Read args from command line.
# send_city():
# python3 weather-client.py "London" "uk" "" ""
# python3 weather-client.py "London" "uk" "metric" "fr"
# send_zip():
# python3 weather-client.py "94040" "us" "imperial" "es"
# seng_geo():
# python3 weather-client.py "51.51" "-0.13" "" ""
if __name__ == '__main__':
    from sys import argv
    send_city(argv[1], argv[2], argv[3], argv[4])
    #send_zip(argv[1], argv[2], argv[3], argv[4])
    #send_geo(argv[1], argv[2], argv[3], argv[4])

