from django.shortcuts import render

# ********* VIEWS *********

def home(request):
    return render(request,'index.html')
