from django.db import models


class Road(models.Model):
    name = models.CharField('Название дороги', max_length=255)
    kod = models.IntegerField('Код дороги', default=0)
    short_name = models.CharField('Краткое имя дороги)', max_length=10, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # куда переадресовывать после изменения
        return f'/rzd/road/{self.id}'

    class Meta:
        ordering = ('name',)
        verbose_name = 'Дорога'
        verbose_name_plural = 'Дороги'
