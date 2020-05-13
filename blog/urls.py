from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post, name="blog"),
    # path('posts', views.post, name="post"),
]
