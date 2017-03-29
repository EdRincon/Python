#! python3
#quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys, pprint

#compute location from command line arguments
if len(sys.argv) > 2:
    print('Usage: quickWeather.py location')
else: sys.exit()

location = ' '.join(sys.argv[1:])

#Download the JSON data from open weather map API
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=7f762997c35608392173c3eb48852ebf' % (location)
response = requests.get(url)
response.raise_for_status()

#Load JSON into a Python variable.
weatherData = json.loads(response.text)

#Prints weather descriptions.
w =  weatherData['list']
print('Current weather in %s: ' % (location))
print(w[0]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print('From', "{0:.2f}".format(float(w[0]['temp']['min']) - 268), 'to', "{0:.2f}".format(float(w[0]['temp']['max']) - 275.15), '°C')
print()
print('Tomorrow')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print('From', "{0:.2f}".format(float(w[1]['temp']['min']) - 268), 'to', "{0:.2f}".format(float(w[1]['temp']['max']) - 275.15), '°C')
print()
print('Day after tomorrow: ')
print(w[2]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print('From', "{0:.2f}".format(float(w[2]['temp']['min']) - 268), 'to', "{0:.2f}".format(float(w[2]['temp']['max']) - 275.15), '°C')
print()

