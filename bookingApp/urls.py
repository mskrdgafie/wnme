from django.urls import path
from . import views

app_name = 'bookingApp'

urlpatterns = [
    # path('main/', admin.site.url),
    path('main/', views.ListCreateServiceProvider.as_view(), name='service_provider_list'),
    path('main/<int:pk>/', views.RetrieveUpdateDestroyServiceProvider.as_view(), name='service_provider_detail'),

    path('main/customer/', views.ListCreateCustomer.as_view(), name='customer_list'),
    path('main/customer/<int:pk>/', views.RetrieveUpdateDestroyCustomer.as_view(), name='customer_detail'),

    path('main/job/', views.ListCreateJobs.as_view(), name='job_list'),
    path('main/job/<int:pk>/', views.RetrieveUpdateDestroyJobs.as_view(), name='job_detail'),

    path('main/order/', views.ListCreateOrder.as_view(), name='order_list'),
    path('main/order/<int:pk>/', views.RetrieveUpdateDestroyOrder.as_view(), name='order_detail'),

    path('main/order-detail/', views.ListCreateOrderDetail.as_view(), name='order_detail_list'),
    path('main/order-detail/<int:pk>/', views.RetrieveUpdateDestroyOrderDetail.as_view(), name='order_detail_detail'),

    path('main/service/', views.ListService.as_view(), name='service_list'),

    path('main/subservice/', views.ListSubService.as_view(), name='sub_service_list'),

]
