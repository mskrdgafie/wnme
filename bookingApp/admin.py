from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.ServiceProvider)
admin.site.register(models.Customer)
admin.site.register(models.Location)
admin.site.register(models.Order)
admin.site.register(models.OrderDetails)
admin.site.register(models.Jobs)
admin.site.register(models.Service)
admin.site.register(models.SubService)
