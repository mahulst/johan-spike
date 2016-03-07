from __future__ import unicode_literals
from django.contrib.gis.db import models
# Create your models here.
from django.contrib.gis import admin



class Entry(models.Model):
    name = models.CharField(max_length=64)
    point = models.PointField(geography=True, spatial_index=True)


admin.site.register(Entry, admin.GeoModelAdmin)