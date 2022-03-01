from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

#from webservice.views import RouteViewSet, TripViewSet
from webservice.views import APIView

router = routers.DefaultRouter()
router.register(r'route', APIView)

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]