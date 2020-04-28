
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('pages.urls')),
    path('cars_list/', include('cars.urls')),
    path('accounts/', include('accounts.urls')),
    path('contact/', include('contacts.urls')),
    path('blog/', include('blog.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
