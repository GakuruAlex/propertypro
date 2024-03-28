from django.db.models import Count
from .models import Property
class PropertyAnnotation:
    def houses_per_property(request):
        properties =Property.objects.annotate(houses_count = Count("houses"))
        return properties