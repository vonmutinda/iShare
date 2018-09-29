from django.shortcuts import render
from .models import Image ,Location , Category

# ********* VIEWS *********

def home(request):
    title = "iShare - Welcome !"
    images = Image.fetch_all()
    locations = Location.fetch_locations()
    categories = Category.fetch_categories() 
    return render(request,'index.html',{ "title":title , "images":images ,"locations":locations ,"categories":categories })

def location(request,location):
    print(location)
    images = Image.get_by_location(location)
    title = location
    breadcrumb = "Location"
    return render(request,'filtered.html', { "images":images , "title":title , "breadcrumb":breadcrumb, })


def category(request,category):
    images = Image.get_by_category(category)
    title = category
    breadcrumb = "Category"
    return render(request,'filtered.html', { "images":images ,"title":title , "breadcrumb": breadcrumb, })

def search_images(request):
    if 'images' in request.GET and request.GET['images']:
        search_term = request.GET.get("images")
        images = Image.search_image(search_term)
        status = f"Displaying images related to {search_term}"
        return render(request , 'filtered.html',  {"status":status , "images":images ,"title":search_term })
    else:
        status = "You haven't queried anything yet !"
        return render(request, "filtered.html",{"status":status})
