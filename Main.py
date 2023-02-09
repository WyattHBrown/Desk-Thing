# desk clock with news headers, the date and time, and the weather. All showing on a 16x2 LCD display.
# notes with a star are elements that have yet to be implemented properly, or are broken
import drivers
from RPLCD import CharLCD
from time import sleep, strftime
import feedparser
import textwrap
import threading
import requests
from requests import get
from datetime import date
from datetime import time
from datetime import datetime
import time
import threading
import requests
import random
import socket
# Here we start the display drivers for the LCD
display = drivers.Lcd()

### USER EDITED VARIABLES ###
# Openweathermap has it's own API, which requires a token, get yours at their website
api_OpenWeather_token=""
# api_OpenWeather_yourCity : Search for your city in openweathermap.org, then put the <city,country> code here with no space in between.
api_OpenWeather_yourCity=""
# RSS Feed on which to get the news header
lin = feedparser.parse("https://gadgets360.com/rss/feeds")
### END OF USER EDITED VARIABLES ###



# this is where it will put the weather output for later, DO NOT PUT ANYTHING HERE
disp_string_weatherInfo=""

# Taken from the raspberry pi guy's sample, demo_scrollingtext.py
# this top row is for the dimensions of the display, and the speed at which to scroll the text (0.1 being the fastest
def long_string(display, text='', num_line=2, num_cols=16, speed=0.19):
    """ 
    Parameters: (driver, string to print, number of line to print, number of columns of your display)
    Return: This function send to display your scrolling string.
    """
    if len(text) > num_cols:
        display.lcd_display_string(text[:num_cols], num_line)
        time.sleep(3)
        for i in range(len(text) - num_cols + 1):
            text_to_print = text[i:i+num_cols]
            display.lcd_display_string(text_to_print, num_line)
            time.sleep(speed)
        time.sleep(1)
    else:
        display.lcd_display_string(text, num_line)



# we set the variable for OWM, keeping it in it's own section so we don't need to start it everytime
def thread_get_weather_info(tokenOWM=api_OpenWeather_token, cityid=api_OpenWeather_yourCity):
    '''
    get the weather info for my city
    '''
    global disp_string_weatherInfo
    while True:
        try:
            base_url='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
            api_OpenWeather_request=requests.get(base_url.format(cityid, tokenOWM))
            api_OpenWeather_json=api_OpenWeather_request.json()
            disp_string_weatherInfo= "   "
            disp_string_weatherInfo=str(round(api_OpenWeather_json['main']['feels_like'])) + "￟C - " + api_OpenWeather_json['weather'][0]['description'] + "   |   " + str(round(api_OpenWeather_json['main']['temp_min'])) + "￟LO - " + str(round(api_OpenWeather_json['main']['temp_max'])) + "￟HI   |   " + str(round(api_OpenWeather_json['main']['humidity']))+ "%   |   " + str(api_OpenWeather_json['wind']['speed']) + "KM/H   |   " + str(api_OpenWeather_json['clouds']['all']) + "% CC     "
            print(str(datetime.now()) + " " + "thr4_weatherinfo got an update: " + disp_string_weatherInfo)
            time.sleep (450)
        except KeyError:
            disp_string_weatherInfo="JSON Key error on weather info response. Check log. Retrying in 5 min."
            print(str(datetime.now()) + " thr4_weatherinfo got an API error. \n" + str(api_OpenWeather_json))
            time.sleep(360)
        except ConnectionError:
            disp_string_weatherInfo="Connection Error while getting the weather info. Will try again in 10 seconds."
            print(str(datetime.now()) + " thr4_weatherinfo got a ConnectionError. will try again in 10 seconds.")
            time.sleep(10)
        except ValueError:
            disp_string_weatherInfo="JSON Decode Error while getting the weather info. Will try again in 20 seconds."
            print(str(datetime.now()) + " thr4_weatherinfo got a ValueError. will try again in 20 seconds.")
            time.sleep(20)
            
                     # CREATING AND CALLING THREADS STARTS HERE
if __name__=="__main__":
                # Start by declaring all these threads
    thr4_weatherinfo=threading.Thread(target=thread_get_weather_info, daemon=True)
                
                # Then we start the threads that populate the variables
disp_string_weatherInfo == ""
thr4_weatherinfo.start()



# This is where we send the info to display, feel free to edit
# amount of times to repeat the nonsense that is this monstrosity
for number in range(150150150):
    # this is where we start the display drivers
        sleep(1)
        # this is how many times it is going to repeat / how many news headers it will get (reccomended 100)
        for i in range(100):
            print (lin['entries'][i]['title'])
            # getting only the title from the RSS news headers, and putting them into the variable name "Text"
            text = lin['entries'][i]['title']
            # splitting the text into X number of rows to show (no longer needed
            split = textwrap.wrap(text, 15)
            sleep(1.5)
            # showing the date
            display.lcd_display_string(strftime('%w %-d %m ' '%H:%M '), 1)
            display.lcd_display_string(strftime('DAT2:%w %d %W %m '), 2)
            sleep(2.7)
            #showing UTC offsync, timezone
            display.lcd_display_string(strftime('%w %-d %m ' '%H:%M '), 1)
            display.lcd_display_string(strftime('UTC3:%z %Z '), 2)
            sleep(2.7)
            #showing the year, days of year passed, and week
            display.lcd_display_string(strftime('%w %-d %m ' '%H:%M '), 1)
            display.lcd_display_string(strftime('YER4:' '%j %W %Y '), 2)
            sleep(2.7)            

            
            #this is where we send the RSS feed and the weather to the display
            display.lcd_display_string(strftime('%w %-d %m ' '%H:%M '), 1)
            long_string(display, text, 2)
            sleep(1.75)
            display.lcd_display_string(strftime('%w %-d %m ' '%H:%M '), 1)
            long_string(display, disp_string_weatherInfo, 2)
            sleep(1.25)
lcd.clear()
lcd.clear()
