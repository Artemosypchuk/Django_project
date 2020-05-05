from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contacts
from cars.models import CarsList
from carmanager.models import CarManager
from django.core.mail import send_mail, EmailMultiAlternatives


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
        manager = CarManager.objects.get(name=car_manager)
        # send_mail(
        #     'New car order',
        #     'Hi' + manager.name + 'You have New order'+' ' + " " + message +
        #     " " + name + " " + car_name + " " + phone,
        #     'artemosipchuk@gmail.com',
        #     [manager.email],
        #     fail_silently=False,

        # )
        subject, from_email, to = 'New car order', 'artemosipchuk@gmail.com', manager.email
        text_content = 'This is an important message.'
        html_content = '<p>' + 'Hi' + ' ' + '<span style="text-transform:uppercase; color:green;">' + manager.name + \
            '</span>'+'<br><hr>' + 'You have New order message: '+' ' + " " + message + \
            "<br><hr>"+'From: ' + name + "<br><hr>" + 'Car: ' + \
            car_name + "<br><hr>"+'Phone: ' + phone + '</p>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        messages.success(request, 'Your reqwest submited!')
        return redirect('accounts:dashboard')
