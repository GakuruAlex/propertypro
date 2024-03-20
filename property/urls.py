from django.urls import path
from property import views

app_name = 'property'

urlpatterns = [
   path('',views.home, name='home'), 
]
