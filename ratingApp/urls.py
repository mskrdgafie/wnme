from django.urls import path
from . import views

app_name = 'ratingApp'

urlpatterns = [
	path('', views.ListCreateRating.as_view(), name="list-rating"),
    path('<int:pk>/', views.RetrieveUpdateDestroyRating.as_view(), name='retrive-update-rating'),
]
