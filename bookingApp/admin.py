from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from . import models

# Register your models here.

@admin.register(models.Location)
class LocationAdmin(OSMGeoAdmin):
    list_display = ('location', 'houseNo', 'description')

admin.site.register(models.ServiceProvider)
admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.OrderDetails)
admin.site.register(models.Jobs)
admin.site.register(models.Service)
admin.site.register(models.SubService)
