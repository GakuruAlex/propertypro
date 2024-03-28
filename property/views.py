from django.forms import ValidationError
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Property,House,WaterBill,ElectricBill
from django.contrib import messages
from django.db.models import F,Sum,Count
from .forms import PropertyForm,HouseForm
from django.db import IntegrityError,transaction
from .functions import MyPaginator
from .annotation_functions import PropertyAnnotation
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
     #Try to get the property objects
    properties_count =Property.objects.count()
    messages.success(request,f"Got {properties_count} properties successfully")
  
    custom_object = PropertyAnnotation()
    properties_q=custom_object.houses_per_property()
    property_page = MyPaginator()
    properties =property_page.make_pages_with_pk(request,query_list=properties_q,items_per_page=6)
        
    
    
    return render(request,'property/properties.html',{'properties':properties})






def property_detail(request,pk):
    """This view gets a particular object based on object id passed from the template

    Args:
        request GET: Fetch object
        pk (int): The primary key from the template is the id of the object to fetch
    """
    annotate_object = PropertyAnnotation()
    properties=annotate_object.houses_per_property()
    
    try:
        property = properties.get(pk=pk)
    except Property.DoesNotExist:
        messages.error(request,f"Property with id {pk} Not Found!")
        return render(request,'property/detail_not_found.html')
    
    houses_q = House.objects.filter(property = property)
    page_obj =MyPaginator()
    
    houses = page_obj.make_pages_with_pk(request,query_list=list(houses_q),items_per_page=str(5))
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
            messages.error(f"Error {form.errors.as_text()}")
            return render(request,"property/create_property.html",{"form":form})
    else:
        form = PropertyForm()
        return render(request,"property/create_property.html",{"form":form})
    
#House model view logic
def view_houses(request):
    houses = House.objects.all()
    
    return render(request,"property/view_houses.html",{"houses":houses})



def house_detail(request,pk,id):
    house =get_object_or_404(House, pk=id)
    return render(request,"property/house_detail.html",{"house":house})


@transaction.atomic #only save if no errors
def add_house(request,pk):
    """_summary_ A view to add a new house to a given property

    Args:
        request (_POST_): _Receive data from the form_
        pk (_int_): _The id of property to add house to_

    Returns:
        _render_: _HTML template_
    """
    if request.method == "POST":#Check if request is POST
        
        property = get_object_or_404(Property,pk=pk)#Get property with given id
        form = HouseForm(request.POST,request.FILES)#initialize form with submitted data and files
        
        if form.is_valid(): #Validation
            #Get form data and set to respective fields
            tenant = form.cleaned_data['tenant']
            rent = form.cleaned_data['rent']
            image = form.cleaned_data['image']
            house_number = form.cleaned_data['house_number']
            category = form.cleaned_data['category']
            owner = form.cleaned_data['owner']
            water_bill =form.cleaned_data['water_bill']
            electric_bill = form.cleaned_data['electric_bill']
            
            #Set status based on whether the house has a tenant
            if tenant == "None":
                status = "AVAILABLE"
            else:
                status ="OCCUPIED"
            #Crete house object with the given attributes
            house=House.objects.create(tenant=tenant,rent=rent,image=image,
                                 house_number=house_number,category=category,
                                 water_bill=water_bill,electric_bill=electric_bill,
                                 property=property,status=status
                                 )
            house.owner.set(owner) #Set house owner
            
            house.save()#Save the house object
            messages.success(request,f"Successfully added {house.house_number} to {property.name}")
            return HttpResponseRedirect(reverse('property:property_detail',args=[pk]))#Redirect to property details
            
        else:#If Validation of submitted data fails
            messages.error(request,f"{form.errors.as_text()}")
            return render(request,"property/add_house.html",{"form":form})
    else:# If request is not POST
        form =HouseForm()
        return render(request,"property/add_house.html",{"form":form})