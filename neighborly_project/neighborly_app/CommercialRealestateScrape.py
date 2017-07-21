from bs4 import BeautifulSoup
import requests
from geopy.geocoders import Nominatim
from selenium import webdriver    #open webdriver for specific browser
from selenium.webdriver.common.keys import Keys   # for necessary browser action
from selenium.webdriver.common.by import By    # For selecting html code
import time

geolocator = Nominatim()

zip_code = 27601
city = 'Raleigh'
state = 'NC'

location = geolocator.geocode("{}, {}".format(city,state))
print(location.latitude)
print(location.longitude)

lat = location.latitude
lon = location.longitude




url= "http://www.cityfeet.com/cont/{}/{}-retail-space?lat={}&lng=-{}#".format(state,city,lat,lon)
headers = {'User-Agent':'Mozilla/5.0'}


with requests.Session() as s:
    s.headers.update(headers)
    
    g = s.get(url)
    soup = BeautifulSoup(g.text, "html.parser")
    soup.pretify
    listings = soup.find_all("div", {'class':"property clearfix src-LN level-30",'class':"property clearfix src-LN level-20"})
    for entry in listings:
        print(entry.find("div",{"class":"row-fluid"}).a.contents)
            
    
