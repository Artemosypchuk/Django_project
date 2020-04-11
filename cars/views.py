from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import CarsList
from .models import CarManager
# Create your views here.


def cars(request):
    carlist = CarsList.objects.all().filter(is_published=True)
    manager = CarManager.objects.all()
    paginator = Paginator(carlist, 3)
    page = request.GET.get("page")
    paged_carlist = paginator.get_page(page)
    context = {
        'carlist': paged_carlist,
        'title': "Our Cars",
        'manager': manager
    }
    return render(request, 'cars/cars.html', context)


def singlecar(request, cars_list_id):
    car = get_object_or_404(CarsList, pk=cars_list_id)
    manager = get_object_or_404(CarManager, name=car.carmanager)
    context = {
        'car': car,
        'manager': manager
    }
    return render(request, 'cars/single_car.html', context)
