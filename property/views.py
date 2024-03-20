from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Property,House,WaterBill,ElectricBill
from django.contrib import messages
# Create your views here.
def home(request):
    try:
        properties = Property.objects.all()
    except Exception as e:
        messages.error(request,f"Error: {e}")
        return render (request,'property/home.html')
    
    return render(request,'property/home.html',{'properties':properties})