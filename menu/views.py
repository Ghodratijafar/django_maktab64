from django.http import request
from django.shortcuts import render
from .models import *
from catagory.models import *
# Create your views here.
def menu_item(request):
    menu = Menuitem.objects.all()
    return render(request, 'menuitems.html', {'menu':menu})