from django.urls import path
from property import views

urlpatterns = [
   path('',views.home, name='home'), 
]
