from django.shortcuts import render

# Create your views here.


def blog(request):
    data = {
        'title': "Blog",
    }
    return render(request, 'blog/blog.html', data)
