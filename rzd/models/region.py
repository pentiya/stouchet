from django.db import models

from rzd.models import Road


class Region(models.Model):
    name = models.CharField('Название региона',max_length=255,)
    kod  = models.IntegerField('Код региона',default=0)
#    road = models.ForeignKey('Road', on_delete=models.PROTECT, blank=True, null=True)
    road = models.ForeignKey(Road, on_delete=models.PROTECT)

    def get_absolute_url(self): #куда переадресовывать после изменения
        return f'/rzd/region/{self.id}'

    class Meta:
        ordering = ('name',)
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.name

