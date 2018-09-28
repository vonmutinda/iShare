from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url , include
from . import views



urlpatterns = [
    url('^$',views.home, name= 'index'),
    url(r'^location/{}/',views.location,name = 'Location'),
    url(r'^category/(\w{4})/$',views.category,name = 'Category'),
    url(r'^search/', views.search_images, name='search_images'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)