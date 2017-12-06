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

import sys
import Adafruit_DHT
import time

while True:

    templist = [];
    humiditylist = [];
    avgtemp = 0;
    avghumidity = 0;

    for x in range(0,15):
        humidity, temperature = Adafruit_DHT.read_retry(11, 4);
        #print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
        templist.append(float(temperature));
        humiditylist.append(float(humidity));
        time.sleep(2);A

    avgtemp = sum(templist) / len(templist);
    avghumidity = sum(humiditylist) / len(humiditylist);

    mydata = open('avgreading.dat', 'w');
    #print('1 Min Avg. Temp = {0:0.1f}c  Humidity = {1:0.1f}%').format(avgtemp, avghumidity);
    mydata.write(('{0:0.1f}c {1:0.1f}%').format(avgtemp, avghumidity));
    mydata.close();

    time.sleep(15);
