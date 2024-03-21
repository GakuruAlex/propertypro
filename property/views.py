from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Property,House,WaterBill,ElectricBill
from django.contrib import messages
# Create your views here.
def home(request):
    """View gets properties saved in the database and serves them to the template

    Args:
        request (GET):GET property objects

    Returns:
        request, template, objects: The given properties are rendered in the Home template
    """
    try: #Try to get the property objects
        properties = Property.objects.all()
    except Exception as e: #Send error to template if get fails
        messages.error(request,f"Error: {e}")
        return render (request,'property/home.html')
    
    return render(request,'property/home.html',{'properties':properties})