from email.mime import image
from django.shortcuts import render
from django.http import HttpResponse
from .models import Images, Location

from images.models import Images

# Create your views here.
def home(request):
    images = Images.objects.all()
    location_list = Location.objects.all()
    return render(request, 'index.html', {"images":images, "location_list": location_list})

def search_category(request):

    location_list = Location.objects.all()

    if 'image' in request.GET and request.GET['image']:
        search_category = request.GET.get('image')
        searched_category = Images.search_image_by_category(search_category)
        message = f"{search_category}"

        return render(request, 'search.html', {"message": message, "images": searched_category, "location_list":location_list})

    else:
        message = "You haven't searched for any catrgory"
        return render(request, 'search.html', {"message": message, "location_list":location_list})

def filter_by_location(request, location):
    images = Images.filter_by_location(location)
    location_list = Location.objects.all()
    return render(request, 'location.html', {"images":images, "location_list":location_list})


