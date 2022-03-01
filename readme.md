# NYC Bike Trips Web Service

This a Django application that serves a web service API for bike trip information in
New York City. 

The app takes in data from a csv provided by City Bike in New York City.

To create the database:

`python3 manage.py makemigrations webservice`

`python3 manage.py migrate webservice`

To extract the data from the csv, run the following command:

`python3 manage.py management_command webservice/management/commands/202201-citibike-tripdata.csv`

To run the app:

`python3 manage.py runserver`

An HTTP API is provided which provides data for list of trips, or a single trip, and allows for filtering by each heading. For example, `http://127.0.0.1:8000/api/trip/?start_station_id=7738.04` gets the trip from the station with id '7738.04.' Similarly, you can filter by each individual route - `http://127.0.0.1:8000/api/trip/?route=2` gets the second trip.

## Requirements

Django 2.2.24

djangorestframework 3.13.1

Python 3.9.7
 
