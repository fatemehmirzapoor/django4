from django.shortcuts import render, get_object_or_404
from .models import Main

def main_list(request):
    posts_all = Main.objects.all()
    return render(request,
                    'main/post/index.html',
                    {'posts': posts_all})
