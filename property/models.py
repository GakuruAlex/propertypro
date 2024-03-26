from django.db import models
from accounts.models import Owner,Tenant

# Create your models here.
# property model
class Property(models.Model):
    name = models.CharField(max_length=25)
    location = models.CharField(max_length=25)

    
    def __str__(self):
        return f"{self.name}"


class House(models.Model):
    VACANCY_CHOICES =[
        ("AVAILABLE",'Available'),
        ("OCCUPIED",'Occupied')
    ]
    CATEGORY =[
        ("SINGLE","single"),
        ("DOUBLE","double_room"),
        ("DOUBLE SELF","double_self"),
        ("ONE BEDROOM","one bedroom"),
        ("TWO BEDROOM","two bedroom"),
    ]

    tenant = models.OneToOneField(Tenant,on_delete=models.CASCADE,null=True,blank=True)
    rent = models.DecimalField(max_digits=9, decimal_places=3)
    image = models.ImageField(upload_to='media/',null=True)
    house_number = models.CharField(max_length= 10)
    status = models.CharField(max_length=20,choices=VACANCY_CHOICES,null=True,blank=True)
    electric_bill =models.ForeignKey('ElectricBill',on_delete=models.CASCADE,null=True,blank=True)
    water_bill = models.ForeignKey('WaterBill',on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=20,choices=CATEGORY)
    property =models.ForeignKey(Property,related_name="houses", on_delete=models.CASCADE,blank=True)
    owner = models.ManyToManyField(Owner,related_name="houses")
    
    def __str__(self):
        return f"{self.house_number}"

class Bill(models.Model):
    account_no = models.IntegerField()
    bill_amount = models.DecimalField(max_digits=9, decimal_places=2)
    bill_month = models.DateField()
    
    def __str__(self):
        return f"Account {self.account_no } Amount: {self.bill_amount}"

class WaterBill(Bill):
    def __str__(self):
        return super().__str__()
class ElectricBill(Bill):
    def __str__(self):
        return super().__str__()

