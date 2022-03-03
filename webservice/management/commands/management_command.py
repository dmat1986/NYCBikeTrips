import csv
import os
import requests
import json

from django.core.management import BaseCommand
from ...models import Route, Trip

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
