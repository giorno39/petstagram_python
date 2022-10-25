from django.urls import path, include

from petstagram.common.views import add_comment
from petstagram.pets.views import add_pet, delete_pet, details_pet, edit_pet

urlpatterns = (
    path('add/', add_pet, name='pet add'),
    path('comment/<int:photo_id>/', add_comment, name="add comment"),
    path('<str:username>/pet/<slug:pet_name>/', include([
        path('', details_pet, name='pet details'),
        path('edit/', edit_pet, name='pet edit'),
        path('delete/', delete_pet, name='pet delete')]
    )))
