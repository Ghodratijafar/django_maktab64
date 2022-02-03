from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView,ListView

from .models import *
from django.views import generic



class OrderList(generic.ListView):
    model = Order
    template_name = 'order.html'


class OrderUpdate(generic.UpdateView):
    model = Order
    template_name = 'o_update.html'
    fields = ['number', 'status', 'timestamp', 'table_id']
    success_url = reverse_lazy('/order')


class OrderCreate(generic.CreateView):
    model = Order
    fields = ['number', 'status', 'timestamp', 'table_id']
    template_name = 'o_create.html'
    success_url = reverse_lazy('/order')


class OrderDelete(generic.DeleteView):
    model = Order

    template_name = 'o_delete.html'
    success_url = reverse_lazy('/order')
