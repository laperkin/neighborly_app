from bs4 import BeautifulSoup
import requests
from geopy.geocoders import Nominatim

geolocator = Nominatim()

zip_code = 27601
city = 'Raleigh'
state = 'NC'

location = geolocator.geocode("{}, {}".format(city,state))
print(location.latitude)
print(location.longitude)

lat = location.latitude
lon = location.longitude


url= "http://www.cityfeet.com/cont/{}/{}-commercial-real-estate?lat={}&lng=-{}#".format(state,city,lat,lon)
headers = {'User-Agent':'Mozilla/5.0'}


with requests.Session() as s:
    s.headers.update(headers)
    
    g = s.get(url)
    soup = BeautifulSoup(g.text, "html.parser")
    soup.pretify
    listings = soup.find_all("div", class_="property clearfix src-LN level-30")
    print(listings)

    
