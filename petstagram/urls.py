from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from petstagram import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('petstagram.accounts.urls')),
    path('', include('petstagram.common.urls')),
    path('pets/', include('petstagram.pets.urls')),
    path('photos/', include('petstagram.photos.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
