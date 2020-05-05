from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    display = ('id', 'title', 'text_area', 'pub_date', 'car_id')
    display_links = ('id', 'title', 'text_area', 'car_id')
    search_filter = ('id', 'pub_date')
    

admin.site.register(Blog, BlogAdmin)
