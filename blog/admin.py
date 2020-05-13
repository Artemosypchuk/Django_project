from django.contrib import admin
from .models import Blog
from .models import Whrite_Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text_area', 'pub_date', 'car_id')
    list_display_links = ('id', 'title', 'text_area', 'car_id')
    list_filter = ('id', 'pub_date')
    

class Whrite_BlogAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'title', 'theme', 'pub_date')
    list_display_links = ('author_name', 'title')
    list_filter = ('id','author_name', 'pub_date')

admin.site.register(Blog,BlogAdmin)
admin.site.register(Whrite_Blog,Whrite_BlogAdmin)
