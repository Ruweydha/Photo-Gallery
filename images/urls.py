from django.urls import URLPattern, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    re_path('^$', views.home, name = 'home'),
    re_path(r'^search/', views.search_category, name ='search'),
    re_path(r'^location/(.*)/$', views.filter_by_location, name = 'location')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)