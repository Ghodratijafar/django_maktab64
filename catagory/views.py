from django.shortcuts import render
from .models import *
# Create your views here.
def categories(request):
    category = Catagory.objects.all()
    return render(request,
                  'category.html',{'category':category} )