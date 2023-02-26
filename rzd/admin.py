from django.contrib import admin

# Register your models here.
from .models import Road
from .models import Region
from .models import Station
from .models import Building

admin.site.register(Road)
admin.site.register(Region)
admin.site.register(Station)
admin.site.register(Building)
