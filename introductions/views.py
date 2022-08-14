from django.shortcuts import render

# Create your views here.


def homeview(request):

    return render(request, "index.html")


def introview(request):

    return render(request, "intro.html")


def mapview(request):

    return render(request, "mapview.html")
