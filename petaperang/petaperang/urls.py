from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

import home.views
from home.views import page_not_found
from petaperang import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maps/', include('maps.urls')),
    path('people/', include('people.urls')),
    path('', include('home.urls')),
    path('login/', home.views.show_login_form, name='login'),
    path('registration/', home.views.registration, name='registration'),
    path('getting_editor/', home.views.getting_editor_rights, name='getting_editor'),
    path('logout/', home.views.logout, name='logout'),
    path('profile/', home.views.profile, name='profile'),
    path('editor/', home.views.show_editor_page, name='editor'),
    path('instruments/', home.views.instruments, name='instruments'),
    path('activate/<uidb64>/<token>/', home.views.activate, name='activate'),
    path('activate/', home.views.activating_form, name='email_activating_form'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found