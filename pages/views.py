from django.shortcuts import render

from cars.models import CarsList
from carmanager.models import CarManager


def index(request):
    carlist = CarsList.objects.all().filter(is_published=True)
    random_car = CarsList.objects.order_by('?')[0]
    context = {
        'carlist': carlist,
        'title': "Our Cars",
        'rnd_car': random_car
    }
    return render(request, 'pages/index.html', context)


def about(request):
    managers = CarManager.objects.all().filter(is_published=True)[:3]
    context = {
        'managers': managers,
        'title': "About Us", 'subcribe': "Some about",
    }
    return render(request, 'pages/about.html', context)


def services(request):
    data = {'title': "Our Services", 'subcribe': "Some services", }
    return render(request, 'pages/services.html', data)


def contactus(request):
    data = {'title': "Contact Us", 'subcribe': "Some contacts", }
    return render(request, 'pages/contactus.html', data)
