# DJANGO
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# LOCAL
from .views import *


app_name = 'homescreen'
urlpatterns = [
    path('', redirect_to_main, name='index'),
    path('projects/', projects, name='projects'),
    path('aboutme/', info, name='basic'),
    path('CV/', render_cv, name='cv')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
