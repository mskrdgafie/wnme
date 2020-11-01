from django.urls import path
from . import views

app_name = 'paymentApp'

urlpatterns = [
	path('', views.payment, name="payment"),
    path('pay-success/', views.paymentAcceptedSuccessfully, name="payment-accepted-sucessfully"),
]
