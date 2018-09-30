from django.shortcuts import render
from .models import Image ,Location , Category

# ********* VIEWS *********

def home(request):
    title = "iShare - Welcome !"
    images = Image.fetch_all()
    locations = Location.fetch_locations()
    categories = Category.fetch_categories() 

    data = {
        'title' : title ,
        'images' : images,
        'locations' : locations,
        'categories' : categories,
    }
    return render(request,'index.html',data)

def location(request,location):
    print(location)
    images = Image.get_by_location(location)
    title = location
    breadcrumb = "Location"
    
    data = {
       "images" : images , 
       "title" : title , 
       "breadcrumb" : breadcrumb, 
    }
    return render(request,'filtered.html', data )


def category(request,category):
    images = Image.get_by_category(category)
    title = category
    breadcrumb = "Category"

    data = {
        "images":images ,
        "title":title , 
        "breadcrumb": breadcrumb,
    }
    return render(request,'filtered.html', data )

def search_images(request):
    if 'images' in request.GET and request.GET['images']:
        search_term = request.GET.get("images")
        images = Image.search_image(search_term)
        status = f"Displaying images related to {search_term}"
        data = {
            "status":status , 
            "images":images ,
            "title":search_term 
        }
        return render(request , 'filtered.html', data )
    else:
        status = "You haven't queried anything yet !"
        return render(request, "filtered.html",{"status":status})
