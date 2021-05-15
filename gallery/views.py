from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def gallery(request):
    images = Image.get_all_images()
    location = Location.object.all()
    return render(request, )
