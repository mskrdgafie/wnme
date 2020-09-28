from django.urls import path
from . import views

app_name = 'chatApp'

urlpatterns = [
    # path('main/', admin.site.url),
    #path('', views.ListCreateServiceProvider.as_view(), name='service_provider_list'),
	path('', views.ListCreateChat.as_view(), name="list-chat"),
    path('<int:pk>/', views.RetrieveUpdateDestroyChat.as_view(), name='retrive-update-chat'),
]
