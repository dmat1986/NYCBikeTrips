from django.db import models
	
#Create the route class
class Route(models.Model):
	ride_id = models.CharField(max_length=20, default="")
	rideable_type = models.CharField(max_length=50, default="")
	start_station_name = models.CharField(max_length=100, default="")
	start_station_id = models.CharField(max_length=10, default="")
	end_station_name = models.CharField(max_length=100, default="")
	end_station_id = models.CharField(max_length=10, default="")
	start_lat = models.CharField(max_length=20, default="")
	start_lng = models.CharField(max_length=20, default="")
	end_lat = models.CharField(max_length=20, default="")
	end_lng = models.CharField(max_length=20, default="")

#Create the Trip class
class Trip(models.Model):
	started_at = models.CharField(max_length=20, default="")
	ended_at = models.CharField(max_length=20, default="")
	route = models.ForeignKey(Route, on_delete=models.CASCADE)
