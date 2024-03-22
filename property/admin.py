from django.contrib import admin
from .models import House,Bill,WaterBill,ElectricBill
# Register your models here.
admin.site.register(House)
admin.site.register(Bill)
admin.site.register(WaterBill)
admin.site.register(ElectricBill)