from django_maktab64.urls import *
from django.urls import path
from .views import *
from django.views.generic import ListView,DeleteView,UpdateView,CreateView

urlpatterns = [
    path('order/', ListView.as_view(model=Order, template_name='order.html')),
    path('o_delete/', DeleteView.as_view(model=Order, template_name='o_delete.html')),
    path('o_update/', UpdateView.as_view(model=Order, template_name='o_update.html')),
    path('o_create/', CreateView.as_view(model=Order, template_name='o_create.html')),
]