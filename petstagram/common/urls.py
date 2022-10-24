from django.urls import path

from petstagram.common.views import index, like_functionality, copy_link_to_clipboard

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_id>/',  like_functionality, name='like_func'),
    path('share/<int:photo_id>/', copy_link_to_clipboard, name='share link'),

)
