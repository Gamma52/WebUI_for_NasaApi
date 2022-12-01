from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from .views import nasa_api


urlpatterns = [
    path('', nasa_api, name='home'),
]
