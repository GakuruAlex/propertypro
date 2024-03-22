from django.db import models
from django.contrib.auth.hashers import make_password,check_password
# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length = 10)
    last_name = models.CharField(max_length = 10)
    identification = models.CharField(unique=True,max_length = 20)
    phone_number = models.CharField(max_length=10)
    avatar =models.ImageField(upload_to='images/')
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

class Tenant(Person):
    def __str__(self):
        return super().__str__()
    
class User(Person,models.Model):
    username = models.CharField(unique=True,max_length = 100)
    password = models.CharField(max_length= 100)
    
    def set_password(self,user_password):
        self.password = make_password(user_password)
    
    def confirm_password(self,user_password):
        return check_password(user_password,self.password)
        
    def __str__(self):
        return super().__str__()

class Employee(User):
    def __str__(self):
        return super().__str__()

class Owner(User):
    def __str__(self):
        return super().__str__()
    