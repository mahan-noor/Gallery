from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Location,Category,Editor

# Create your views here.

def gallery(request):
    images = Image.get_all_images()
    category = Category.objects.all()
    locations = Location.objects.all()
    return render(request, 'gallery.html', {"images":images, "locations":locations , "category":category})



def search_results(request):
    categories = Category.objects.all()
    location = Location.objects.all()
    if 'image' in request.GET and request.GET['image']:
        image_category = request.GET.get('image')
        searched_images = Image.search_by_category

        message = f"{image_category}"

        return render(request, 'search.html', {"message":message , "images": searched_images, "categories": categories, "locations":locations})

    else:
        message: "you have not searched for any term"
        return render(request,'search.html' ,{"message":message ,"locations":locations})


def singlepost(request,img_id):
    try:
        singlepost = Image.objects.get(id = img_id)
    except DoesNotExist:
        raise Http404()
    return render (request,"singlepost.html", {"singlepost": singlepost}) 

def location_filter(request, location):
    locations = Location.objects.all()
    images = Image.objects.filter(location__id = location)
    title = 'Location Photos'
    return render(request, 'location.html', {'title':title, 'images':images, 'locations':locations})

