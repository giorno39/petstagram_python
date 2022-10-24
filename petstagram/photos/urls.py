from django.urls import path, include

from petstagram.photos.views import photo_add, photo_details, photo_edit, photo_delete

urlpatterns = (
    path('add/', photo_add, name='add photo'),
    path('<int:pk>/', include([
        path('', photo_details, name='details photo'),
        path('edit/', photo_edit, name='edit photo'),
        path('delete/', photo_delete, name='delete photo'),
    ]))
)
