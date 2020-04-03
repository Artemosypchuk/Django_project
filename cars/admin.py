from django.contrib import admin

from .models import CarsList


class CarListAdmin(admin.ModelAdmin):
    list_display = ("id", "vendor", "model", "engine", "color",
                    "price", "is_published", "carmanager_id", "rating")
    list_display_links = ("id", "vendor", "model")

    list_editable = ("is_published",)

    search_fields = ("vendor", "model", "engine",
                     "price", "rating")
    list_per_page = 25
    list_filter = ("model", "carmanager_id", "price")


admin.site.register(CarsList, CarListAdmin)
