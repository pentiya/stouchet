from django.contrib import admin

# Register your models here.
from .models import Road
from .models import Region
from .models import Station
from .models import Building


# admin.site.register(Road)
class RoadAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'kod')
    #list_filter = ['road']
#   ordering = ('name')
admin.site.register(Road, RoadAdmin)


# admin.site.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'road', 'kod',)


    list_filter =['road',]
# ordering = {'name',}
admin.site.register(Region, RegionAdmin)

admin.site.register(Station)
admin.site.register(Building)
