from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.gallery,name = 'gallery'),
    path('search/', views.search_results,name='search_results'),
    re_path('singlepost/(?P<img_id>\d+)',views.singlepost,name='singlepost' ),
    re_path('location/(?P<location_id>\d+)',views.location_filter,name ='location')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)