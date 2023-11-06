from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect_to_home_page),
    path('home/', views.show_home_page, name='home')
]
