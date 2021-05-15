from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.

def gallery(request):
    images = Image.get_all_images()
    location = Location.object.all()
    return render(request, )
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
