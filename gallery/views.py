from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Location,Category,Editor


# Create your views here.

def gallery(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request, 'gallery.html', {"images":images, "locations":locations})



def search_results(request):
    
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        category = Category.objects.get(name=search_term)
        searched_images = Image.search_by_category(category)
        

        message = f"{category}"

        return render(request, 'search.html', {"message":message , "images": searched_images})

    else:
        message: "you have not searched for any term"
        return render(request,'search.html' ,{"message":message ,"locations":locations})


def singlepost(request,img_id):
    try:
        singlepost = Image.objects.get(id = img_id)
    except DoesNotExist:
        raise Http404()
    return render (request,"singlepost.html", {"singlepost": singlepost}) 

def location_filter(request, location_id):
    locations = Location.objects.get(id=location_id)
    images = Image.search_by_location(locations)
    title = 'Location Photos'
    return render(request, 'location.html', {'title':title, 'images':images, 'locations':locations})

