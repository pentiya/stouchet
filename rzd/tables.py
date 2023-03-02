import django_tables2 as tables

from .models import Road
from .models import Region
from .models import Station


class RoadTable(tables.Table):
    model = Road
    template_name = 'django_tables2/bootstrap.html'
    fields = ("name",)
    # fields = __all_


class RegionTable(tables.Table):
    model = Region
    template_name = 'django_tables2/bootstrap.html'
    fields = ("name",)


class StationTable(tables.Table):
    model = Station
    template_name = 'django_tables2/bootstrap.html'
    fields = ("name",)
