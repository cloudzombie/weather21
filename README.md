# weather21
Weather API endpoint for the 21 Bitcoin Computer.

$ 21 buy url "http://10.244.132.211:5050/weather/city?cityname=London&countrycode=uk&unit=metric"

$ 21 buy url "http://10.244.132.211:5050/weather/zip?zipcode=94040&countrycode=us&unit=imperial&lang=es"

$ 21 buy url "http://10.244.132.211:5050/weather/geo?latitude=51.51&longitude=-0.13"

Or download and run the weather client:

$ wget -O weather.py http://10.244.132.211:5050/weather/client

$ python3 weather.py "London" "uk" "metric" "en"
