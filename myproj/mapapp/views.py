from django.shortcuts import render

# Create your views here.
def map(request):
    return render(request,"mapapp/map.html")
def central(request):
    return render(request,"mapapp/central.html")   
def temple(request):
    return render(request,"mapapp/temple.html")
def stadium(request):
    return render(request,"mapapp/stadium.html")
def museum(request):
    return render(request,"mapapp/museum.html")
def highcourt(request):
    return render(request,"mapapp/highcourt.html")