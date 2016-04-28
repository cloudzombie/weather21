#!/usr/bin/env python3

import os
import requests
import logging
import yaml
import json

from flask import Flask
from flask import request
from flask import send_from_directory

# Import from the 21 Bitcoin Developer Library
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

# Set up logging
log = logging.getLogger('werkzeug')
logging.basicConfig(filename='weather.log',level=logging.DEBUG)
#log.setLevel(logging.ERROR)

# Configure the app and wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

SERVER_PORT = '5050'

OWM_API_KEY = os.environ.get('OPEN_WEATHER_MAP_API_KEY')
OWM_CURRENT_URL = 'http://api.openweathermap.org/data/2.5/'
OWM_MODES= ['weather', 'forecast']

# Provide the app manifest to the 21 crawler.
@app.route('/weather/manifest')
def manifest():
    with open('./manifest.yaml', 'r') as f:
        manifest = yaml.load(f)
    return json.dumps(manifest)

# Provide an example client script.
@app.route('/weather/client')
def client():
   return send_from_directory('static', 'weather.py')

# Charge a fixed fee per request to the /city current weather endpoint
@app.route('/weather/current/city')
@payment.required(2500)
def current_city_weather():
   # the parameters sent by the client
   cityname = str(request.args.get('cityname'))
   countrycode = str(request.args.get('countrycode'))
   unit = str(request.args.get('unit'))
   lang = str(request.args.get('lang'))

   if countrycode:
      cityparams = cityname + ',' + countrycode
   else:
      cityparams = cityname

   if unit:
      unitparam = unit
   else:
      unitparam = "standard"

   if lang:
      langparam = lang
   else:
      langparam = "en"

   userdata = {"q": cityparams, "units": unitparam, "lang": langparam, "APPID": OWM_API_KEY}
   resp = requests.get(OWM_CURRENT_URL + OWM_MODES[0], params=userdata)

   return resp.text

# Charge a fixed fee per request to the /zip current weather endpoint
@app.route('/weather/current/zip')
@payment.required(2500)
def current_zip_weather():
   # the parameters sent by the client
   zipcode = str(request.args.get('zipcode'))
   countrycode = str(request.args.get('countrycode'))
   unit = str(request.args.get('unit'))
   lang = str(request.args.get('lang'))

   cityparams = zipcode + ',' + countrycode

   if unit:
      unitparam = unit
   else:
      unitparam = "standard"

   if lang:
      langparam = lang
   else:
      langparam = "en"

   userdata = {"zip": cityparams, "units": unitparam, "lang": langparam, "APPID": OWM_API_KEY}
   resp = requests.get(OWM_CURRENT_URL + OWM_MODES[0], params=userdata)

   return resp.text

# Charge a fixed fee per request to the /geo current weather endpoint
@app.route('/weather/current/geo')
@payment.required(2500)
def current_geo_weather():
   # the parameters sent by the client
   latitude = request.args.get('latitude')
   longitude = request.args.get('longitude')
   unit = str(request.args.get('unit'))
   lang = str(request.args.get('lang'))

   if unit:
      unitparam = unit
   else:
      unitparam = "standard"

   if lang:
      langparam = lang
   else:
      langparam = "en"

   userdata = {"lat": latitude, "lon": longitude, "units": unitparam, "lang": langparam, "APPID": OWM_API_KEY}
   resp = requests.get(OWM_CURRENT_URL + OWM_MODES[0], params=userdata)

   return resp.text

# Charge a fixed fee per request to the /city forecast weather endpoint
@app.route('/weather/forecast/city')
@payment.required(2500)
def forecast_city_weather():
   # the parameters sent by the client
   cityname = str(request.args.get('cityname'))
   countrycode = str(request.args.get('countrycode'))
   unit = str(request.args.get('unit'))
   lang = str(request.args.get('lang'))

   if countrycode:
      cityparams = cityname + ',' + countrycode
   else:
      cityparams = cityname

   if unit:
      unitparam = unit
   else:
      unitparam = "standard"

   if lang:
      langparam = lang
   else:
      langparam = "en"

   userdata = {"q": cityparams, "units": unitparam, "lang": langparam, "APPID": OWM_API_KEY}
   resp = requests.get(OWM_CURRENT_URL + OWM_MODES[1], params=userdata)

   return resp.text

# Charge a fixed fee per request to the /zip forecast weather endpoint
@app.route('/weather/forecast/zip')
@payment.required(2500)
def forecast_zip_weather():
   # the parameters sent by the client
   zipcode = str(request.args.get('zipcode'))
   countrycode = str(request.args.get('countrycode'))
   unit = str(request.args.get('unit'))
   lang = str(request.args.get('lang'))

   cityparams = zipcode + ',' + countrycode

   if unit:
      unitparam = unit
   else:
      unitparam = "standard"

   if lang:
      langparam = lang
   else:
      langparam = "en"

   userdata = {"zip": cityparams, "units": unitparam, "lang": langparam, "APPID": OWM_API_KEY}
   resp = requests.get(OWM_CURRENT_URL + OWM_MODES[1], params=userdata)

   return resp.text

# Charge a fixed fee per request to the /geo forecast weather endpoint
@app.route('/weather/forecast/geo')
@payment.required(2500)
def forecast_geo_weather():
   # the parameters sent by the client
   latitude = request.args.get('latitude')
   longitude = request.args.get('longitude')
   unit = str(request.args.get('unit'))
   lang = str(request.args.get('lang'))

   if unit:
      unitparam = unit
   else:
      unitparam = "standard"

   if lang:
      langparam = lang
   else:
      langparam = "en"

   userdata = {"lat": latitude, "lon": longitude, "units": unitparam, "lang": langparam, "APPID": OWM_API_KEY}
   resp = requests.get(OWM_CURRENT_URL + OWM_MODES[1], params=userdata)

   return resp.text

# Initialize and run the server
if __name__ == '__main__':
    #app.run(host='0.0.0.0', debug=True)
    #app.run(host='0.0.0.0')
    app.run(host='0.0.0.0', port=SERVER_PORT)
