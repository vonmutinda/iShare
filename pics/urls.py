from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url , include
from . import views



urlpatterns = [
    url(r'^$',views.home, name= 'index'),
    url(r'^location/(\w{2,})/$',views.location,name = 'location'), 
    url(r'^category/(\w+)/$',views.category,name = 'category'),
    url(r'^search/', views.search_images, name='search_images'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


'''
TAKE AWAY

Look closely at urlpatters , so to grab a word from the url and pass it as an argument use 
(\w+) regex === this expects as many words as possible

(\w{2,}) ==== this expects a word with a minum of 2 chars
(\w{2,10}) === a minimum of 2 maximum of 10 character word
'''