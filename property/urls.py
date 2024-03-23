from django.urls import path
from property import views

app_name = 'property'

urlpatterns = [
   path('',views.home, name='home'),
   path('properties/',views.properties_list,name="properties"),
   path("properties/<int:pk>/",views.property_detail,name="property_detail"),
   path("properties/create-property/",views.create_property,name="create_property"),
]
