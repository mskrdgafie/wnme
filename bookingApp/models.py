from datetime import timezone

from django.db import models
from django.conf import settings


# Create your models here.
class Location(models.Model):
    lat = models.DecimalField(decimal_places=4, max_digits=20)
    lng = models.DecimalField(decimal_places=10, max_digits=20)
    houseNo = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


class ServiceProvider(models.Model):
    IS_ONLINE = (
        ('online', 'Online'),
        ('offline', 'Offline'),
    )
    GENDER = (
        ('man', 'Man'),
        ('woman', 'Woman'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    is_online = models.CharField(max_length=100, choices=IS_ONLINE, default='offline')
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER, default='')
    workingRadius = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.user.username)


class Customer(models.Model):
    IS_ONLINE = (
        ('online', 'Online'),
        ('offline', 'Offline'),
    )
    GENDER = (
        ('man', 'Man'),
        ('woman', 'Woman'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    is_online = models.CharField(max_length=100, choices=IS_ONLINE, default='offline')
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER, default='')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.user.username)


class Service(models.Model):
    serviceTitle = models.CharField(max_length=100)  # ex. home cleaning
    icon = models.ImageField(upload_to='icon/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('serviceTitle',)
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def __str__(self):
        return '{}'.format(self.serviceTitle)


class SubService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    subServiceTitle = models.CharField(max_length=100)  # ex.

    def __str__(self):
        return '{}'.format(self.subServiceTitle)

    class Meta:
        ordering = ('subServiceTitle',)

    def __str__(self):
        return '{}'.format(self.subServiceTitle)


class Jobs(models.Model):
    subService = models.ForeignKey(SubService, on_delete=models.CASCADE)
    serviceProvider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    max_booking = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.subService.subServiceTitle)


class Order(models.Model):
    PAYMENT_TYPE = (
        ('cash', 'Cash'),
        ('paypal', 'Paypal'),
    )
    SCHEDULE = (
        ('now', 'Now'),
        ('later', 'Later'),
    )

    ORDER_STATUS = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('go_to_customer', 'Go to customer'),
        ('arrived', 'Arrived'),
        ('start_work', 'Start work'),
        ('completed', 'Completed'),
    )
    serviceProvider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    deliveryAddress = models.ForeignKey(Location, on_delete=models.CASCADE)
    additionalRemark = models.TextField()
    paymentType = models.CharField(max_length=20, choices=PAYMENT_TYPE)
    scheduleType = models.CharField(max_length=20, choices=SCHEDULE)
    scheduleDate = models.DateTimeField()
    orderStatus = models.CharField(max_length=100, choices=ORDER_STATUS, default='pending')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity