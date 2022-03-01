from rest_framework import viewsets, generics
import django_filters.rest_framework

from webservice.serializers import TripSerializer

from webservice.models import Route, Trip

class APIView(generics.ListAPIView):
    model = Trip
    serializer_class = TripSerializer

    def get_queryset(self):
        queryset = Trip.objects.all()
        route = self.request.query_params.get('route', None)
        if route is not None:
         queryset = queryset.filter(route=route)
        return queryset
    #set filters for each field
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

 