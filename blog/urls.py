from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('post-list/', views.post_list, name='post_list'),
]
