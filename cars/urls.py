from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.cars, name="cars_list"),
    path('<int:cars_list_id>/', views.singlecar, name="single_car")
]
