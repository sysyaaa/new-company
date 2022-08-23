from django.core.paginator import Paginator
from django.shortcuts import render
from . import models


def pcaseview(request):
    page = request.GET.get("page", "1")
    pcase_list = models.PrevCases.objects.order_by("-create_date")
    paginator = Paginator(pcase_list, 4)
    page_obj = paginator.get_page(page)
    context = {"pcase_list": page_obj}
    return render(request, "pcases.html", context)


def pcase_detailview(request, pk):

    pcase = models.PrevCases.objects.get(pk=pk)
    context = {"pcase": pcase}
    return render(request, "pcase_detail.html", context)
