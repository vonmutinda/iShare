from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url , include
from . import views



urlpatterns = [
    url(r'^$',views.home, name= 'index'),
    url(r'^location/(\w{2,})/$',views.location,name = 'location'),
    url(r'^category/(\w{2,})/$',views.category,name = 'category'),
    url(r'^search/', views.search_images, name='search_images'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)