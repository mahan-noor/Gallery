from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.gallery,name = 'gallery'),
    path('search/', views.search_results,name='search_results'),
    path('location/(\d+',views.location_filter,name ='location')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)