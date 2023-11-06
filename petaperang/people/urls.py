
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_people, name='people'),
    path('introduction/', views.person_introduction, name='person_introduction'),
    path('search/', views.people_ssearch, name='person_search'),
    path('edit/<slug:slug>', views.personality_editing, name='personality_editing'),
    path('<slug:slug>/', views.personality_page, name='personality_page')
]

