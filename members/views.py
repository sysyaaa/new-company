from django.shortcuts import render


def member_intro(request):
    # 변호사 소개
    return render(request, "members/members.html")
