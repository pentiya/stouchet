from django.db import models
from django.contrib.auth.models import User



class Road(models.Model):
    name = models.CharField('Название дороги', max_length=255)
    kod = models.IntegerField('Код дороги', default=0)
    short_name = models.CharField('Краткое имя дороги)', max_length=10, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_by_user')
#    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='updated_by_user')
    def __str__(self):
        return self.name

    def get_absolute_url(self):  # куда переадресовывать после изменения
        return f'/rzd/road/{self.id}'

    class Meta:
        ordering = ('name',)
        verbose_name = 'Дорога'
        verbose_name_plural = 'Дороги'
