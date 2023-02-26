from django.db import models

from rzd.models import Region


class Station(models.Model):
    name = models.CharField('Станция', max_length=255, )
    kod = models.IntegerField('Код станции', default=0)
    csvt = models.IntegerField('Код АСУ ЦСВТ', default=0)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    rvc = models.IntegerField('РВЦ', default=0)
    lon = models.FloatField('Долгота', default=0)
    lat = models.FloatField('Широта', default=0)

    def get_absolute_url(self):  # куда переадресовывать после изменения
        return f'/rzd/station/{self.id}'

    class Meta:
        ordering = ('name',)
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'

    def __str__(self):
        return self.name
