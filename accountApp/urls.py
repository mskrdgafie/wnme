from django.urls import path
from . import views

app_name = 'accountApp'

urlpatterns = [
    # path('main/', admin.site.url),
    #path('', views.ListCreateServiceProvider.as_view(), name='service_provider_list'),
	path("users/", views.UserCreate.as_view(), name="user_create"),
    path('login/', views.LoginView.as_view(), name='login'),
]
