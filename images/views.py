from django.shortcuts import render
from django.http import HttpResponse
import images

from images.models import Images

# Create your views here.
def home(request):
    images = Images.objects.all()
    return render(request, 'index.html', {"images":images})

def search_category(request):

    if 'image' in request.GET and request.GET['image']:
        search_category = request.GET.get('image')
        searched_category = Images.search_image_by_category(search_category)
        message = f"{search_category}"

        return render(request, 'search.html', {"message": message, "images": searched_category})

    else:
        message = "You haven't searched for any catrgory"
        return render(request, 'search.html', {"message": message})



