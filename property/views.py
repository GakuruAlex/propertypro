from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Property,House,WaterBill,ElectricBill
from django.contrib import messages
from django.db.models import F,Sum,Count
from .forms import PropertyForm,HouseForm
from django.db import IntegrityError,transaction
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
        properties_count =Property.objects.count()
        properties=Property.objects.annotate(house_count=Count("houses"))
        messages.success(request,f"Got {properties_count} properties successfully")
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
    
    try:
        property = Property.objects.get(pk=pk)
    except Property.DoesNotExist:
        messages.error(request,f"Property with id {pk} Not Found!")
        return render(request,'property/detail_not_found.html')
    houses = House.objects.filter(property = property)
   
    
    return render(request,'property/property_detail.html',{"property":property, "houses":houses})



@transaction.atomic
def create_property(request):
    """Create a new property view

    Args:
        request POST: Create property

    Returns:
        render:initially property form else created property template
    """
   
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"Created Property Successfully!")
            return HttpResponseRedirect(reverse("property:properties"))
    else:
        form = PropertyForm()
        return render(request,"property/create_property.html",{"form":form})
    
#House model view logic
def view_houses(request):
    houses = House.objects.all()[:8]
    
    return render(request,"property/view_houses.html",{"houses":houses})



def house_detail(request,pk,id):
    house =get_object_or_404(House, pk=id)
    return render(request,"property/house_detail.html",{"house":house})

@transaction.atomic
def add_house(request,pk):
    
    if request.method == "POST":
        property = get_object_or_404(Property,pk=pk)
        form = HouseForm(request.POST,request.FILES)
        if form.is_valid():
            tenant = form.cleaned_data['tenant']
            rent = form.cleaned_data['rent']
            image = form.cleaned_data['image']
            house_number = form.cleaned_data['house_number']
            category = form.cleaned_data['category']
            owner = form.cleaned_data['owner']
            water_bill =form.cleaned_data['water_bill']
            electric_bill = form.cleaned_data['electric_bill']
            
            if tenant == "None":
                status = "AVAILABLE"
            else:
                status ="OCCUPIED"
            
            house=House.objects.create(tenant=tenant,rent=rent,image=image,
                                 house_number=house_number,category=category,
                                 water_bill=water_bill,electric_bill=electric_bill,
                                 property=property,status=status
                                 )
            house.owner.set(owner)
            house.save()
            messages.success(request,f"Successfully added {house.house_number} to {property.name}")
            return HttpResponseRedirect(reverse('property:property_detail',args=[pk]))
        else:
            messages.errors(request,f"{form.errors.as_data()}")
            return render(request,"property/add_house.html",{"form":form})
    else:
        form =HouseForm()
        return render(request,"property/add_house.html",{"form":form})