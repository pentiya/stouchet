from django.db import models

import datetime
from django.utils import timezone

tz = timezone.get_default_timezone()



class Vendor(models.Model):
    kod = models.IntegerField('код')
    name = models.CharField('производитель')

    class Meta:
        ordering = ('name')
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField('имя устройства', max_length=50)
    ip = models.GenericIPAddressField('адрес')
    #    model = models.ForeignKey('DeviceModel', on_delete=models.PROTECT, blank=True, null=True,)
    ser_num = models.CharField('серийный номер', max_length=50)
    inv_num = models.CharField('инвентарный номер', max_length=50)
    #    usel = models.ForeignKey('ivc.Usel', on_delete=models.PROTECT)
    #    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(default=timezone.now)


#   date_opros = models.DateTimeField()
#    active = models.BooleanField(default=True)
....


class Meta:
    ordering = ['name']
    verbose_name = 'Устройство'
    verbose_name_plural = 'Устройства'


def __str__(self):
    return self.name

.

def changed(self):
    return "aaaaa"


#       return format(self.changed.strftime(%Y-%m-%d %H:%M)).
# format(self.created.astimezone(tz).strftime('%d.%m.%Y %H:%M'))

"""

class DeviceModel(models.Model):
    name = models.CharField('имя', max_length = 50)
    model = models.CharField('модель', max_length = 50)
    vendor = models.ForeignKey('Vendor', on_delete=models.PROTECT, blank=True, null=True,)
#   device = models.ForeignKey('Device', on_delete=models.PROTECT, blank=True, null=True)
#   date = models.DateTimeField('дата изменеия')

    class Meta:.
        ordering = ('model',)
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'.

class PartNumber(models.Model):
    part_number = models.CharField('парт-номер', max_length = 50)
    vendor = models.ForeignKey('Vendor', on_delete=models.PROTECT, blank=True, null=True,)
    model = models.ForeignKey('DeviceModel', on_delete=models.PROTECT, blank=True, null=True,)
    kod = models.CharField('код', max_length = 50)

    class Meta:.
        ordering = ('part_number',).
        verbose_name = 'Парт-номер'
        verbose_name_plural = 'Парт-номера'.


class DeviceInterface(models.Model):
    name = models.CharField('имя устройства', max_length = 50)
    device = models.ForeignKey('Device', on_delete=models.PROTECT, blank=True, null=True)
#   date = models.DateTimeField('дата изменеия')

    class Meta:.
        ordering = ('name',).
        verbose_name = 'Интерфейс'
        verbose_name_plural = 'Интерфейсы'.

    def __str__ (self):
        return self.name

class DeviceHistory(models.Model):
#    date = models.DateTimeField('дата изменения')
    device = models.ForeignKey('Device', on_delete=models.CASCADE, blank=True, null=True)
    usel = models.ForeignKey('ivc.Usel', on_delete=models.PROTECT, blank=True, null=True)
    comment = models.CharField('комментарий', max_length = 50)
.
#class DeviceInterfaceHistory(models.Model):
#    date = models.DateTimeField('дата изменения')
#    old_device = models.ForeignKey('Device', on_delete=models.CASCADE, blank=True, null=True)
#    new_device = models.ForeignKey('Device', on_delete=models.CASCADE, blank=True, null=True)
#    comment = models.CharField('имя устройства', max_length = 50)



"""
