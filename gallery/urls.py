from django.urls import path

from . import views

urlpatterns=[
    path('',views.gallery,name = 'gallery'),
    path('search/', views.search_results,name='search_results'),
    path('location/(\d+',views.location_filter,name ='location')

]