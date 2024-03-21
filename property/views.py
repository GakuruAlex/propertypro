from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Property,House,WaterBill,ElectricBill
from django.contrib import messages
from django.db.models import F,Sum
# Create your views here.
def home(request):
    return HttpResponse(f"Simplify Manage")
def properties_list(request):
    """View gets properties saved in the database and serves them to the template

    Args:
        request (GET):GET property objects

    Returns:
        request, template, objects: The given properties are rendered in the Home template
    """
    try: #Try to get the property objects
        properties = Property.objects.all()[:5]
        properties_count =Property.objects.count()
        messages.success(request,f"Got {properties_count} properties successful")
    except Exception as e: #Send error to template if get fails
        messages.error(request,f"Error: {e}")
        return render (request,'property/properties.html')
    
    return render(request,'property/properties.html',{'properties':properties})

def property_detail(request,pk):
    """This view gets a particular object based on object id passed from the template

    Args:
        request GET: Fetch object
        pk (int): The primary key from the template is the id of the object to fetch
    """
    property = get_object_or_404(Property,pk=pk)
    return render(request,'property/property_detail.html',{"property":property})