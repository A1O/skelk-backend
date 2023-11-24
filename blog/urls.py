from django.urls import path
from .views import dashboard, post_list, profile_list, profile


app_name = 'blog'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile_list/', profile_list, name='profile_list'),
    path('profile/<int:pk>', profile, name='profile'),
    path('dg/', post_list, name='post_list'),
]
