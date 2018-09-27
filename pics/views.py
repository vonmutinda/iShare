from django.shortcuts import render

# ********* VIEWS *********

def home(request):
    title = "iShare - Welcome !"
    
    return render(request,'index.html',{"title":title})
