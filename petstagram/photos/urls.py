from django.urls import path, include

from petstagram.photos.views import photo_add, photo_details, photo_edit

urlpatterns = (
    path('add/', photo_add, name='add photo'),
    path('<int:pk>/', include([
        path('', photo_details, name='details photo'),
        path('edit/', photo_edit, name='edit photo'),
    ]))
)
