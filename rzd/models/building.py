from django.db import models
from rzd.models import Station
class Building(models.Model):
    name = models.CharField('Здание',max_length=255,)
#    kod = models.IntegerField(default=0)
    Station = models.ForeignKey(Station, on_delete=models.PROTECT)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'

    def __str__(self):
        return self.name
