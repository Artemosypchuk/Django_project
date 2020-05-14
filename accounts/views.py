from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contacts
from cars.models import CarsList

# from django.shortcuts import render, redirect
# from django.contrib import messages, auth
# from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username alrady taken.")
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email alrady taken.")
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(
                        username=username, email=email, password=password, first_name=first_name, last_name=last_name,)
                    user.save()
                    messages.success(request, "You are registred. Log in")
                    return redirect('accounts:login')
        else:
            messages.error(request, "Passwords do not match")
        return redirect('accounts:register')
    else:
        return render(request, "accounts/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are logged in")
            logged_in = True
            return redirect('accounts:dashboard')
        else:
            messages.error(request, "Login or password incorrect")
            return redirect('accounts:login')
    else:
        return render(request, "accounts/login.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
    messages.success(request, "See you later!")
    return redirect("index")


def dashboard(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        orders = Contacts.objects.all().filter(user_id=user_id)

        listed_cars = CarsList.objects.all()
        context = {
            'orders': orders,
            'listed_cars': listed_cars
        }

    return render(request, "accounts/dashboard.html", context)
