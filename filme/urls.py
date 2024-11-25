# Para cada pág criada do site, tem que fazer 3 coisas:
#   1- url;
#   2- view;
#   3- template

from django.urls import path, include
from .views import homepage

urlpatterns = [
    path('', homepage),
] 
