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
import os
import time
import re
import datetime

from Adafruit_LED_Backpack import AlphaNum4

display = AlphaNum4.AlphaNum4()
display.begin()

thetemp="";
thehumidity="";
thetime="";
message="";
pos = 0
osd=1;

while True:

    mydata = open('avgreading.dat', 'r');
    (thetemp,thehumidity) = mydata.read().split(' ');
    #print(thetemp);
    #print(thehumidity);
    mydata.close();

    # Display the Temperature for 7 seconds
    display.clear();
    decimalpos=thetemp.find('.');
    thetemp=re.sub('[.]','',thetemp);
    display.print_str(thetemp[pos:pos+4])
    display.set_decimal(decimalpos-1,1)
    display.write_display()
    time.sleep(7);

    # Display the Humidity for 7 seconds
    display.clear();
    decimalpos=thehumidity.find('.');
    thehumidity=re.sub('[.]','',thehumidity);
    display.print_str(thehumidity[pos:pos+4])
    display.set_decimal(decimalpos-1,1)
    display.write_display()
    time.sleep(7);

    # Display the Time for 7 seconds
    display.clear();
    thetime=('{:%H:%M}'.format(datetime.datetime.now().time()));
    decimalpos=thetime.find(':');
    thetime=re.sub('[:]','',thetime);
    display.print_str(thetime[pos:pos+4])
    for x in range(0,7) :
        showdecimal=0;
        showdecimal=x%2;
        display.set_decimal(decimalpos-1,showdecimal)
        display.write_display()
        time.sleep(1);

