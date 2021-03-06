# WeatherSleuth
Pull data via Python from Aercus Instruments Wireless Weather Station WeatherSleuth.

The Developers/Admins use case is for a WebTechnologies - https://www.bangor.ac.uk/computer-science-and-electronic-engineering/postgraduate-modules/ICE-4111 - module to incorporate the data
into a customized website via Javascript calls into the Postgres database, of course
you can use it however you like :)

This is the first iteration and will post modifications as I go (scope to move/create functions)

## Requirements

Built on Ubuntu/OSX, but should work fine on Windows, just change clear to cls for the sys call

Python Packages 
 - bs4
 - requests
 - os

Aercus Instruments Wireless Weather Station WeatherSleuth

I purchased mine from Amazon, other retailers are available

https://www.amazon.co.uk/gp/product/B00ZVFZUS6

# Running
Modify the URL value to the IP address of your server (blue box with lights)
```
#globals
# URL to curl values from, pull the max
URL="http://YOURWEATHERSLUTHEIP/livedata.htm"
```

The script is self contained and running in a loop. The simpliest way is to just call the script
```
python3 scrape-weather.py
```
Whereby it will loop around scraping stats from the weathersluthe server
```
 Measurement             Value 
 -----------             ----- 
 Current Time            11:16 3/6/2021 
 Indoor Temp             22.8 
 Indoor Humidty          36 
 Absolute Pressure       1034.20 
 Realtive Pressure       1022.60 
 Outdoor Temperature     7.3 
 Outdoor Humidity        50 
 Wind Direction          50 
 Wind Speed              2.2 
 Wind Gust               4.0 
 Solar Radiation         485.77 
 UV                      412 
 UVI                     1 
 Rain Hourly             0.00 
 Rain Weekly             2.70 
 Rain Monthly            2.70 
 Rain Yearly             22.20 
 ```
 
 ## variables 
 The variables are documented, but for completeness are given here.
 
 ```
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
```
This allows to bolt on other modules (pandas/postgres,etc) to use the values as you please.
