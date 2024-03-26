from django.urls import path
from property import views

app_name = 'property'

urlpatterns = [
   path('',views.home, name='home'),
   #Properties urls
   path('properties/',views.properties_list,name="properties"),
   path("properties/<int:pk>/",views.property_detail,name="property_detail"),
   path("properties/create-property/",views.create_property,name="create_property"),
   
   #Houses urls
   path("properties/<int:pk>/houses/<int:id>/",views.house_detail,name="house_detail"),
   path("properties/<int:pk>/add-house/",views.add_house,name="add_house")
   
]
