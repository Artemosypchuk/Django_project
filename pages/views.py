from django.shortcuts import render
from blog.models import Blog
from cars.models import CarsList
from carmanager.models import CarManager
from django.core.paginator import Paginator


def index(request):
    carlist = CarsList.objects.all().filter(is_published=True)
    vendor_search = CarsList.objects.order_by('vendor').distinct('vendor')
    model_search = CarsList.objects.order_by('model').distinct('model')
    engine_search = CarsList.objects.order_by('engine').distinct('engine')
    transmission_search = CarsList.objects.order_by('transmission').distinct('transmission')
    blog_list = Blog.objects.all().order_by('-pub_date')
    posted_car = CarsList.objects.all()
    random_car = CarsList.objects.order_by('?')[0]
    context = {
        'carlist': carlist,
        'title': "Our Cars",
        'rnd_car': random_car,
        'vendor_search': vendor_search,
        'model_search': model_search,
        'engine_search': engine_search,
        'transmission_search': transmission_search,
        'blog_list': blog_list,
        'posted_car': posted_car,
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


def search(request):
    query = CarsList.objects.order_by('vendor')
    vendor_search = CarsList.objects.order_by('vendor').distinct('vendor')
    model_search = CarsList.objects.order_by('model').distinct('model')
    engine_search = CarsList.objects.order_by('engine').distinct('engine')
    transmission_search = CarsList.objects.order_by('transmission').distinct('transmission')
    carlist = CarsList.objects.all().filter(is_published=True)
    if 'vendor' in request.GET:
        vendor = request.GET["vendor"]
        if vendor:
            query = query.filter(vendor__iexact=vendor)
    if 'model' in request.GET:
        model = request.GET["model"]
        if model:
            query = query.filter(model__iexact=model)

    if 'engine' in request.GET:
        engine = request.GET["engine"]
        if engine:
            query = query.filter(engine__iexact=engine)

    if 'transmission' in request.GET:
        transmission = request.GET["transmission"]
        if transmission:
            query = query.filter(transmission__iexact=transmission)
    context = {
        'carlist_search': query,
        'carlist': carlist,
        'vendor_search': vendor_search,
        'model_search': model_search,
        'engine_search': engine_search,
        'transmission_search': transmission_search,
    }
    return render(request, 'pages/search.html', context)



def post(request):
    blog_list = Blog.objects.all().order_by('-pub_date')
    posted_car = CarsList.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get("page")
    paged_blog_list = paginator.get_page(page)
    context = {
        'blog_list': paged_blog_list,
        'posted_car': posted_car
    }
    return render(request, 'pages/index.html', context)