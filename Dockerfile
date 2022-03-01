# pull the official base image
FROM python:3.9.7

# create work directory
RUN mkdir /NYCBikeTrips

# set work directory
WORKDIR /NYCBikeTrips

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY . /django_projects1

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
