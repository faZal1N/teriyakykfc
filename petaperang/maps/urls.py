from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_maps, name='maps'),
    path('introduction/', views.event_introduction, name='event_introduction'),
    path('search/', views.event_search, name='event_search'),
    path('search_id/', views.event_search_id, name='event_search_id'),
    path('search_local_maps/', views._search_local_maps, name='event_search_local_maps'),
    path('search_participants/', views._search_participants, name='event_participants'),
    path('edit/local_map/<slug:slug>', views.edit_local_map, name='edit_local_map'),
    path('edit/<slug:slug>', views.event_editing, name='event_editing'),
    path('local_map_creator', views.local_map_creator, name='local_map_creator'),
    path('<slug:slug>/', views.event_page, name='event_page'),

]
