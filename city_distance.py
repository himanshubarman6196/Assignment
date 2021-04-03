from math import sin, cos, sqrt, atan2, radians
import re
import logging

logging.basicConfig(level = logging.INFO)
valid_city = "51.5074 N, 0.1278 W"

class FindDistance:
	def __init__(self,first_city,second_city):
		self.first_city  = first_city
		self.second_city = second_city


	def find_distance(self):
		""" regex for pattern matching for valid latitude and longitude input """
		pattern = r"(\d+\.\d+)\s*\S\,\s*(\d+\.\d+)\s*\S"
		""" radius of earth """
		R = 6373.0
		
		try:
			City_1 = re.search(pattern, self.first_city)
			City_2 = re.search(pattern, self.second_city)
			""" fetching matched group from both variables """
			
			lat1 = radians(float(City_1.group(1)))
			lon1 = radians(float(City_1.group(2)))
			lat2 = radians(float(City_2.group(1)))
			lon2 = radians(float(City_2.group(2)))
			dlon = lon2 - lon1
			dlat = lat2 - lat1

			a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
			c = 2 * atan2(sqrt(a), sqrt(1 - a))

			""" rounding of whole value to 2 decimal point """
			distance = round(R * c,2)
		except Exception as e:
			return f'Distance not found due to {e} try entering valid pattern for {valid_city}'
		return f"City 1 and City 2 are {distance} Km apart"


if __name__ == '__main__':
	city_1 = input("Please enter the lattitude and longitude for city 1-> ")
	city_2 = input("Please enter the lattitude and longitude for city 2-> ")
	distance_obj = FindDistance(city_1,city_2).find_distance()
	print(distance_obj)




