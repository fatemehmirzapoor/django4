from .models import Main
from django.shortcuts import render, get_object_or_404

def main_list(request):
    posts_all = Main.objects.all()
    return render(request,'main/post/index.html',{'posts': posts_all})

