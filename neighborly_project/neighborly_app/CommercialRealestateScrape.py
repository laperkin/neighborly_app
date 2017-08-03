from bs4 import BeautifulSoup
import requests
from geopy.geocoders import Nominatim
import time


def get_listings(city,state):
	geolocator = Nominatim()
	location = geolocator.geocode("{}, {}".format(city,state))

	lat = location.latitude
	lon = location.longitude

	url= "http://www.cityfeet.com/cont/{}/{}-retail-space?lat={}&lng=-{}#".format(state,city,lat,lon)
	headers = {'User-Agent':'Mozilla/5.0'}


	with requests.Session() as s:
		s.headers.update(headers)
		g = s.get(url)
		soup = BeautifulSoup(g.text, "html.parser")
		soup.pretify
		listings = soup.find_all("div", class_=["property clearfix src-LN level-30","property clearfix src-LN level-20","property clearfix src-LN level-10"])
		list_matrix = []
		for entry in listings:
			row=[]
			row.append(entry.find("div",{"class":"row-fluid"}).a.contents)
			address=entry.select('address')
			for div in address:
				row.append(div.find('div').text) 
			list_matrix.append(row)
	return list_matrix



            
    
