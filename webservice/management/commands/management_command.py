import csv
import os
import requests
import json
from math import cos, asin, sqrt
import dateutil.parser as parser

from django.core.management import BaseCommand
from ...models import Route, Trip

#Gets weather conditions and temperature based on starting latitude,
#starting longitude, and start time of trip
def get_weather(lat,lng,started_at):
   url = 'https://api.weather.gov/points/'+lat+','+lng
   r = requests.get(url)
   r=r.json()
   gridid=r["properties"]["gridId"]
   gridx=r["properties"]["gridX"]
   gridy=r["properties"]["gridY"]
   gridid=str(gridid)
   gridx=str(gridx)
   gridy=str(gridy)
   obs_url = 'https://api.weather.gov/gridpoints/'+gridid+'/'+gridx+','+gridy+'/stations'
   g=requests.get(obs_url)
   gg=g.json()
   dataArray=gg["features"]
   list_ = []
   v_lat = []
   v_lng = []

   count = len(dataArray)

   for j in range(count):
      for i in dataArray:
         v_lat.append(float(i["geometry"]["coordinates"][1]))
         v_lng.append(float(i["geometry"]["coordinates"][0]))
      list_.append({'lat':v_lat[j],'lng':v_lng[j]})

   #Finds the nearest coordinates using the Haversine formula
   def distance(lat1, lon1, lat2, lon2):
      p = 0.017453292519943295
      hav = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
      return 12742 * asin(sqrt(hav))
   def closest(data, v):
      return min(data, key=lambda p: distance(v['lat'],v['lng'],p['lat'],p['lng']))

   our_data = {'lat':float(lat),'lng':float(lng)}
   comp_data = list_
   closest_coord = closest(comp_data,our_data)

   nearest_lat = closest_coord["lat"]
   nearest_lng = closest_coord["lng"]

   for i in dataArray:
      if float(i["geometry"]["coordinates"][1]) == nearest_lat and float(i["geometry"]["coordinates"][0]) == nearest_lng:
         station = i["id"]

   station = requests.get(station)
   station = station.json()
   station_name = station["properties"]["stationIdentifier"]
   date = parser.parse(started_at)
   started_at=date.isoformat()
   started_at=started_at+'Z'
   cond_url='https://api.weather.gov/stations/'+station_name+'/observations?start='+started_at+'&limit=1'
   cond = requests.get(cond_url)
   cond = cond.json()
   condition = cond["features"][0]["properties"]["textDescription"]
   temp = cond["features"][0]["properties"]["temperature"]["value"]

   return [condition,temp]

#Reads the data from the csv and write it into the database
class Command(BaseCommand):
	help = "Loads data from CitiBike csv"
	

	def add_arguments(self, parser):
		parser.add_argument("file_path", type=str)

	def handle(self, *args, **options):
		file_path = options["file_path"]
		with open(file_path, "r") as csv_file:
			data = csv.reader(csv_file, delimiter=",")
			next(data)
			routes = {route_.ride_id: route_ for route_ in Route.objects.all()}
			trips = []
			for row in data:
				route_ride_id = row[0]
				route = routes.get(route_ride_id)
				if not route:
					route = Route.objects.create(
						ride_id=row[0],
						rideable_type=row[1], 
						start_station_name=row[4],
						start_station_id=row[5],
						end_station_name=row[6],
						end_station_id=row[7],
						start_lat=row[8],
						start_lng=row[9],
						end_lat=row[10],
						end_lng=row[11])
					routes[route.ride_id] = route
				trip = Trip(
					started_at=row[2],
					ended_at=row[3],
					#conditions=get_weather(route.start_lat,route.start_lng,route.started_at)[0],
					#temperature=get_weather(route.start_lat,route.start_lng,route.started_at)[1],
					route=route)
				trips.append(trip)
				if len(trips) > 5000:
					Trip.objects.bulk_create(trips)
					trips = []
			if trips:
				Trip.objects.bulk_create(trips)


				
		self.stdout.write(
			self.style.SUCCESS(
				f"Loading CSV succeeded."
			)
		)
