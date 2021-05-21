# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import shop
def shop_list(request):
        shops_all = shop.objects.all()
        return render(request,'shop/post/list.html',{'posts': shops_all})
