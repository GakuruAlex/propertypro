from django.contrib import admin
from .models import Tenant,Owner,User,Employee,Person
# Register your models here.
admin.site.register(Owner)
admin.site.register(Tenant)
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Person)