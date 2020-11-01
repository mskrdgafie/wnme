from django.db import models

# Create your models here.
class YenePay(models.Model):
    total_amount = models.CharField(max_length=100)
    buyer_id= models.CharField(max_length=500)
    marchant_order_id= models.CharField(max_length=500)
    marchant_id= models.CharField(max_length=500)
    merchant_code= models.CharField(max_length=500)
    transaction_code= models.CharField(max_length=500)
    transaction_id= models.CharField(max_length=500)
    status= models.CharField(max_length=100)
    currency= models.CharField(max_length=100)
    signature= models.CharField(max_length=1000)