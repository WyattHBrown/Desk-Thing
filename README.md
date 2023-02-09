# Desk-Thing
A small little desk feed to keep you up to date on (almost) anything you might care about.
This is a small little project that I have been working on in my spare time for a while. It is very janky, but because I have been working on it in the background for a long time I decided to release my child to you, the GitHub community, for feedback!
it is very very rough, some things could dramatically be done better. As long as it works, I'm happy.
I borrowed some code from [Raspberry pi guy's lcd library](https://github.com/the-raspberry-pi-guy/lcd) to get the scrolling text to work with weather and [feedparser](https://pypi.org/project/feedparser/)

### What it uses:

- A raspberry Pi (I have been using a Pi 4, I havent tested others)
- An i2C character display (I have a 16x2 LCD, you can change the display type in Main.py

### What it does:
- Displays the Date and time, as well as the time zone and other specific date formats such as the year and date to year
- Displays the weather (using OpenWeatherMap API)
- Displays the news (via FeedParser)
- Displays other random information from your choice
- Can display a custom message of your choice
- and more!

The News feed uses RSS, and loads the most recent news headlines, it also loops a certain number of times (set to 150150150 just to keep it going for as long as possible)

### Requirements

This project requires you to enable I2C in your raspberry pi settings, do so by doing:
- `sudo raspi-config`
- Interface options
- Enable i2c interface
depending on what type of Pi you have, or what type of display you have, it might be different on how you set it up.

you will need to use pip to install requirements, the ones I downloaded are:
[RPLCD](https://pypi.org/project/RPLCD/)
time
[Feedparser](https://pypi.org/project/feedparser/)

You will also need to get an OpenWeatherMap API Key
you also need to place 
### How to use:
- Open Main.py
- the variables are marked at the top, fill them out as wanted
- you can also add or remove sections based off of the example chunk
- you can also add or remove weather sections based off of the JSON from OWM
- once you have filled out the sections, it should be able to see all of your provided information!

### Thanks To:
- [Raspberry pi guy's lcd library](https://github.com/the-raspberry-pi-guy/lcd)
- [feedparser](https://pypi.org/project/feedparser/)

### To Be Completed:
- [ ] Clean up code
- [ ] Remove unnecessary code and dependencies
- [ ] Add stocks for no reason
- [ ] fix up readme
- [ ] sort files properly
- [x] add time
- [x] add weather
- [x] convert to Pi guy's API

if you wish to see anything else please let me know!
