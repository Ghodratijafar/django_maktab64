from django_maktab64.urls import *
from .views import *
urlpatterns = [
    path('categories/', categories),
]