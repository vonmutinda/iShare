from django.shortcuts import render
from .models import Image

# ********* VIEWS *********

def home(request):
    title = "iShare - Welcome !"
    images = Image.fetch_all()
    return render(request,'index.html',{ "title":title , "images":images , })

