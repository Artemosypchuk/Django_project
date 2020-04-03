from django.contrib import admin

from .models import CarManager


class CarManagersAdmin(admin.ModelAdmin):
    list_display = ("name", "phone")
    list_display_links = ("name", "phone")
    search_fields = ("name", "phone")
    list_per_page = 25


admin.site.register(CarManager, CarManagersAdmin)
