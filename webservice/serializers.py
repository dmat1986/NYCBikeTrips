from rest_framework import serializers
import requests
import json

from webservice.models import Route, Trip


#Serialize the tables and join them in preparation for outputting the API data
class TripSerializer(serializers.ModelSerializer):
       ride_id = serializers.CharField(source='route.ride_id')
       rideable_type = serializers.CharField(source='route.rideable_type')
       start_station_name = serializers.CharField(source='route.start_station_name')
       start_station_id = serializers.CharField(source='route.start_station_id')
       end_station_name = serializers.CharField(source='route.end_station_name')
       end_station_id = serializers.CharField(source='route.end_station_id')
       start_lat = serializers.CharField(source='route.start_lat')
       start_lng = serializers.CharField(source='route.start_lng')
       end_lat = serializers.CharField(source='route.end_lat')
       end_lng = serializers.CharField(source='route.end_lng')

       class Meta:
         model = Trip
         fields = (
            'ride_id',
            'rideable_type',
            'started_at', 
            'ended_at',
            'start_station_name',
            'start_station_id',
            'end_station_name',
            'end_station_id',
            'start_lat',
            'start_lng',
            'end_lat',
            'end_lng',
            'route')
       
