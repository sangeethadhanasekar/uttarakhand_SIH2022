import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

api_key = "5c4ae535d70641bbb1563343222102"


def weather_info(movie_name):
    url = "http://api.weatherapi.com/v1/current.json?key=" + api_key + "&q=" + movie_name + "&aqi=no"
    weather = requests.get(url).json()
    localtime = weather['location']['localtime']
    temp_c = weather['current']['temp_c']
    temp_f = weather['current']['temp_f']
    condition_text = weather['current']['condition']['text']
    condition_icon = weather['current']['condition']['icon']
    return (localtime, temp_f, temp_c, condition_text, condition_icon)
    #print(weather['location']['localtime'])
    #print(weather['current']['temp_c'])
    #print(weather['current']['temp_f'])
    #print(weather['current']['condition']['text'])
    #print(weather['current']['condition']['icon'])


#weather_info("Udham Singh Nagar")
