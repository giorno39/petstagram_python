from django.urls import path, include

from petstagram.accounts.views import register_user, login_user, profile_user, edit_user, delete_user

urlpatterns = (
    path('login/', login_user, name='user login'),
    path('register/', register_user, name='user register'),
    path('profile/<int:pk>/', include([
        path('', profile_user, name='user profile'),
        path('edit/', edit_user, name='user edit'),
        path('delete/', delete_user, name='user delete')
    ]))
)
