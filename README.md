# Desk-Thing
A small little desk feed to keep you up to date on (almost) anything you might care about.

<img alt="Project Status: Active – The project has reached a stable, usable state and is being actively developed." src="https://www.repostatus.org/badges/latest/active.svg"> <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/WyattHBrown/Desk-Thing?logo=python&logoColor=yellow"> <img alt="website" src="https://img.shields.io/badge/Website-Vestbot.ca-blueviolet"> <img alt="Version" src="https://img.shields.io/github/v/release/Wyatthbrown/Desk-thing"> <img alt="License" src="https://img.shields.io/github/license/WyattHBrown/Desk-Thing"> <img alt="Last Update" src="https://img.shields.io/github/last-commit/WyattHBrown/Desk-Thing"> <img alt="Issues" src="https://img.shields.io/github/issues/WyattHBrown/desk-thing"> <img alt="Issues closed" src="https://img.shields.io/github/issues-closed/WyattHBrown/desk-thing">

This is a small little project that I have been working on in my spare time for a while. It is very janky, but because I have been working on it in the background for a long time I decided to release my child to you, the GitHub community, for feedback!
it is very very rough, some things could dramatically be done better. As long as it works, I'm happy.
I borrowed some code from [Raspberry pi guy's lcd library](https://github.com/the-raspberry-pi-guy/lcd) to get the scrolling text to work with weather and [feedparser](https://pypi.org/project/feedparser/)

### What it uses:

- A raspberry Pi (I have been using a Pi 4, I havent tested others)
- An i2C character display (I have a 16x2 LCD, you can change the display type in Main.py)

### What it does:
- Displays the Date and time, as well as the time zone and other specific date formats such as the year and date to year
- Displays the weather (using OpenWeatherMap API)
- Displays the news (via FeedParser)
- Displays other random information from your choice
- Can display a custom message of your choice
- and more!

The News feed uses RSS. It takes just the most recent News headlines from that RSS (however many you want is changeable in the code) it also loops a certain number of times (set to 150150150 just to keep it going for as long as possible)

# Requirements

1. This project requires you to enable I2C in your raspberry pi settings, do so by doing:
- `sudo raspi-config`
- Interface options
- Enable i2c interface
- connect your i2c display! (depending on what type of Pi you have, or what type of display you have, it might be different on how you set it up.)\

2. the python requirements are
- time
- [Feedparser](https://pypi.org/project/feedparser/)
- threading
- requests

if you don't have them, you can use pip to isntall them via the terminal
3. You will also need to get an OpenWeatherMap API Key

### How to use:
- Open Main.py
- edit the variables to your liking (the required ones to edit are at the top after imports, for easy access
- you can also add or remove weather sections based off of what is already there (check out the JSON to see what you can get!)
- once you have filled out the sections, it should be able to see all of your provided information!

## Thanks To:
- [Raspberry pi guy's lcd library](https://github.com/the-raspberry-pi-guy/lcd)
- [feedparser](https://pypi.org/project/feedparser/)

## To Be Completed:
Check the issues tab!
