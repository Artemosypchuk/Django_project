from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Blog, Whrite_Blog

from cars.models import CarsList

# Create your views here.


def blog(request):
    if request.method == 'POST':
        author_id = request.POST['author_id']
        car_id = request.POST['car_id']
        car_name = request.POST['car_name']
        text_area = request.POST['text_area']
        if request.user.is_authenticated:
            has_contacted = Blog.objects.all().filter(
                text_area=text_area, author_id=author_id
            )
            if has_contacted:
                messages.error(request, 'Post already Published!')
                return redirect('accounts:dashboard')

        post = Blog(author_id=author_id, text_area=text_area,
                    title=car_name, car_id=car_id)
        post.save()
        messages.success(request, 'Your Post will be moderated!')

        return redirect('accounts:dashboard')


def post(request):
    blog_list = Whrite_Blog.objects.all().order_by('-pub_date')
    paginator = Paginator(blog_list, 1)
    page = request.GET.get("page")
    paged_blog_list = paginator.get_page(page)
    context = {
        'blog_list': paged_blog_list,
    }
    return render(request, 'blog/blog.html', context)
