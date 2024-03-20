from django.db import models
from accounts.models import Owner,Tenant

# Create your models here.
# property model
class Property(models.Model):
    name = models.CharField(max_length=25)
    location = models.CharField(max_length=25)
    no_houses = models.IntegerField()
    houses = models.ForeignKey('House',on_delete=models.CASCADE)
    owner = models.ManyToManyField(Owner,related_name='properties')

class House(models.Model):
    VACANCY_CHOICES ={
        "AVAILABLE":'Available',
        "OCCUPIED":'Occupied'
    }
    CATEGORY = {
        "SINGLE":'single',
        "DOUBLE":'double-room',
        "DOUBLE SELF":'double-self',
        "ONE BEDROOM":'one bedroom',
        "TWO BEDROOM":'two bedroom'
    }
    tenant = models.OneToOneField(Tenant)
    rent = models.FloatField()
    image = models.ImageField(upload_to='media/')
    house_number = models.CharField(max_length= 10)
    status = models.CharField(max_length=20,choices=VACANCY_CHOICES)
    electric_bill =models.ForeignKey('ElectricBill',on_delete=models.CASCADE)
    water_bill = models.ForeignKey('WaterBill',on_delete=models.CASCADE)
    category = models.CharField(max_length=20,choices=CATEGORY)
