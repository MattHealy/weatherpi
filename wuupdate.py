#!/usr/bin/python
#
# ==================================== #
#
# Author: Kevin H.  18/11/2017
#
# Re-use Allowed If
# Crediting Original Author
#
# ==================================== #

import re
import requests

# --------------------------------------

def celsius_to_fahrenheit(c):
    return (c * 1.8) + 32.0

# --------------------------------------

def fahrenheit_to_celsius(f):
    return (f - 32.0) * 0.555556

# --------------------------------------

def calc_dewpoint(temp, hum):
    c = fahrenheit_to_celsius(temp)
    x = 1 - 0.01 * hum;

    dewpoint = (14.55 + 0.114 * c) * x;
    dewpoint = dewpoint + ((2.5 + 0.007 * c) * x) ** 3;
    dewpoint = dewpoint + (15.9 + 0.117 * c) * x ** 14;
    dewpoint = c - dewpoint;

    return celsius_to_fahrenheit(dewpoint)

# --------------------------------------

def calc_heat_index(temp, hum):
    if (temp < 80):
        return temp
    else:
        return -42.379 + 2.04901523 * temp + 10.14333127 * hum - 0.22475541 * \
        temp * hum - 6.83783 * (10 ** -3) * (temp ** 2) - 5.481717 * \
        (10 ** -2) * (hum ** 2) + 1.22874 * (10 ** -3) * (temp ** 2) * \
        hum + 8.5282 * (10 ** -4) * temp * (hum ** 2) - 1.99 * \
        (10 ** -6) * (temp ** 2) * (hum ** 2);

# --------------------------------------

mydata = open('avgreading.dat', 'r');
(thetemp,thehumidity) = mydata.read().split(' ');
mydata.close();

thetemp=float(re.sub('[c]','',thetemp));
thehumidity=re.sub('[%]','',thehumidity);

thetemp = (thetemp * 1.8) + 32;
feelslike = calc_heat_index(float(thetemp), float(thehumidity));
thedewpoint = calc_dewpoint(float(thetemp), float(thehumidity));
thetemp = str(thetemp);
stationid = "STATION123"; #UPDATE WITH YOUR PWS STATION ID
stationpwd = "PASSWORD"; #UPDATE WITH YOUR PWS STATION PASSWORD

url = 'https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?ID=' + stationid + '&PASSWORD=' + stationpwd + '&dateutc=now&action=updateraw&tempf=' + thetemp + '&humidity=' + thehumidity + '&dewptf=' + str(thedewpoint);

response = requests.get(url);
print('Response: ' + str(response.status_code) + ' ' + str(response.text));


