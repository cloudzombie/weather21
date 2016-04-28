# weather21
Weather API endpoint for the 21 Bitcoin Computer.

Get current weather by city name, by zip code or by geographic coordinates:

$ 21 buy url "http://10.244.132.211:5050/weather/current/city?cityname=London&countrycode=uk&unit=metric"

$ 21 buy url "http://10.244.132.211:5050/weather/current/zip?zipcode=94040&countrycode=us&unit=imperial&lang=es"

$ 21 buy url "http://10.244.132.211:5050/weather/current/geo?latitude=51.51&longitude=-0.13"

Get forecast weather by city name, by zip code or by geographic coordinates:

$ 21 buy url "http://10.244.132.211:5050/weather/forecast/city?cityname=London&countrycode=uk&unit=metric"

$ 21 buy url "http://10.244.132.211:5050/weather/forecast/zip?zipcode=94040&countrycode=us&unit=imperial&lang=es"

$ 21 buy url "http://10.244.132.211:5050/weather/forecast/geo?latitude=51.51&longitude=-0.13"

Or download and run the weather client:

$ wget -O weather.py http://10.244.132.211:5050/weather/client

$ python3 weather.py "current" "London" "uk" "metric" "en"

$ python3 weather.py "forecast" "London" "uk" "imperial" "es"
