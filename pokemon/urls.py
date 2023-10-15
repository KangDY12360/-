from django.urls import path
from .views import pokemon_list
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('list/', pokemon_list, name='pokemon_list'),
]
