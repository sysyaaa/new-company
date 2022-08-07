from django.shortcuts import render

# Create your views here.


def workscope_list(request):
    # 업무분야
    return render(request, "workscopes.html")
