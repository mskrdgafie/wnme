from django.db import models
from bookingApp.models import Order, Customer, ServiceProvider

# Create your models here.
class Rating(models.Model):
    RATER_CHOICES = (
        ('customer', 'Customer'),
        ('service_provider', 'Service Provider'),
    )
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    rater = models.CharField(max_length=100, choices=RATER_CHOICES, default='customer')
    rating = models.IntegerField()
    comment = models.TextField()
