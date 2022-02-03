from django_maktab64.urls import *
from .views import *
urlpatterns = [
    path('hello/', hello),
    path('brand/', create_brand,name='create_brand'),
]