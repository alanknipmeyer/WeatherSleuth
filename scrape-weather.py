
# Author - Alan Knipmeyer, provided free without warranty on the MIT license
"""
Copyright (c) 2021, Alan Knipmeyer
All rights reserved.
This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree. 
"""

# import libraries
from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime,timedelta
import os
#import psycopg2


# one big function currently
def getweather(URL):
    """Gets weatherdata via http

    Parameters
    ----------
    URL of the measurement server

    Returns
    -------
    time - format is "hh:mm m/d/y"
    intemp - float temp in celsius from internal measurement device
    inhumi - humidty in bars from from internal measurement device
    abspress - float of the absolute pressure from internal measurement device
    relpress - float of the realtive pressure
    outtemp - exterior temperature as record by external instrument
    outhumi - percentage value of outdoor humity 
    windir - direction of the wind 0= Northt, then as a clock face, i.e. 90=E, 180=S, 270=W
    windspeed - float of the current windspeed ()
    gustspeed - float of the gust speed
    solarrrad - Solar Radiation captured by Solar Panel as a float value
    uv - ultraviolet as a float from external measurement device (solar panel)
    uvi - ultraviolet integer index as calculated from external measurement device (solar panel)
    rainofhourly - float value of amount of rain collected in mm in the current hour from external device - can be wrong due to spiders who like to sleep in there
    rainofweekly - float value of amount of rain collected in mm in the current week from external device
    rainofmonthly - float value of amount of rain collected in mm in the current month from external device
    rainofyearly - float value of amount of rain collected in mm in the current year from external device
    """
    # URL to curl values from, pull the max
    #URL="http://192.168.1.138/livedata.htm"
    # Make a GET request to fetch the raw HTML content
    page = requests.get(URL)
    # Parse the html content
    soup = BeautifulSoup(page.content, "html.parser")
  
    # extrapolate values from html via name tage and value pair
    CurrTime = soup.find('input',{'name':'CurrTime'})['value']
    InTemp = soup.find('input',{'name':'inTemp'})['value']
    InHumi = soup.find('input',{'name':'inHumi'})['value']
    AbsPress = soup.find('input',{'name':'AbsPress'})['value']
    RelPress = soup.find('input',{'name':'RelPress'})['value']
    outTemp = soup.find('input',{'name':'outTemp'})['value']
    outHumi = soup.find('input',{'name':'outHumi'})['value']
    windir = soup.find('input',{'name':'outHumi'})['value']
    windspeed = soup.find('input',{'name':'windspeed'})['value']
    gustspeed = soup.find('input',{'name':'gustspeed'})['value']
    solarrad = soup.find('input',{'name':'solarrad'})['value']
    UV = soup.find('input',{'name':'uv'})['value']
    UVI = soup.find('input',{'name':'uvi'})['value']
    rainofhourly = soup.find('input',{'name':'rainofhourly'})['value']
    rainofweekly = soup.find('input',{'name':'rainofweekly'})['value']
    rainofmonthly = soup.find('input',{'name':'rainofmonthly'})['value']
    rainofyearly = soup.find('input',{'name':'rainofyearly'})['value']

    # output values
    print ( "\n",
            "Measurement \t\t Value \n",
            "----------- \t\t ----- \n"
            " Current Time \t\t",CurrTime,"\n",
            "Indoor Temp \t\t",InTemp,"\n",
            "Indoor Humidty \t",InHumi,"\n",
            "Absolute Pressure  \t",AbsPress,"\n",
            "Realtive Pressure  \t",RelPress,"\n",
            "Outdoor Temperature  \t",outTemp,"\n",
            "Outdoor Humidity  \t",outHumi,"\n",
            "Wind Direction  \t",windir,"\n",
            "Wind Speed  \t\t",windspeed,"\n",
            "Wind Gust  \t\t",gustspeed,"\n",
            "Solar Radiation \t", solarrad,"\n",
            "UV \t\t\t", UV,"\n",
            "UVI \t\t\t", UVI,"\n",
            "Rain Hourly \t\t", rainofhourly,"\n",
            "Rain Weekly \t\t", rainofweekly,"\n",
            "Rain Monthly \t\t", rainofmonthly,"\n",
            "Rain Yearly \t\t", rainofyearly,"\n"
            )

#globals
# URL to curl values from, pull the max
URL="http://YOURWEATHERSLUTHEIP/livedata.htm"
# call functions
while 1==1:
    getweather(URL)
    time.sleep(300)    
    os.system('clear')
