from django.db import models
from bookingApp.models import Customer, ServiceProvider

# Create your models here.

class Chat(models.Model):
    SENDER_CHOICES = (
        ('customer', 'Customer'),
        ('service_provider', 'Service Provider'),
    )
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sender = models.CharField(max_length=100, choices=SENDER_CHOICES, default='notset')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
            return self.text