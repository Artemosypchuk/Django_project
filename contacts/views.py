from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contacts
from cars.models import CarsList


def contact(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        car_id = request.POST['car_id']
        name = request.POST['name']
        car_name = request.POST['car_name']
        email = request.POST['email']
        car_manager = request.POST['car_manager']
        phone = request.POST['phone']
        message = request.POST['message']
        if request.user.is_authenticated:
            has_contacted = Contacts.objects.all().filter(
                car_id=car_id, user_id=user_id
            )
            if has_contacted:
                messages.error(request, 'Car allready rented')
                return redirect('accounts:dashboard')

        contact = Contacts(car=car_name, car_id=car_id, phone=phone, name=name,
                           message=message, email=email, user_id=user_id)
        contact.save()
        one_car = CarsList.objects.get(id=car_id)
        one_car.is_published = False
        one_car.save()
        messages.success(request, 'Your reqwest submited!')
        return redirect('accounts:dashboard')
