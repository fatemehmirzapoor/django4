# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import shop
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

def shop_list(request):
        object_list = shop.objects.all()
        paginator = Paginator(object_list, 5) # 5 posts in each page
        
        try:
                page = request.GET.get('page')
        except:
                page=1

        try:
                posts = paginator.page(page)
        except PageNotAnInteger:
        # If page is not an integer deliver the first page
                posts = paginator.page(1)
        except EmptyPage:
        # If page is out of range deliver last page of results
                posts = paginator.page(paginator.num_pages)

        return render(request,
                        'shop/post/list.html',
                        {'page': page,
                        'posts': posts})

def shop_detail(request, year, month, day, post):
        post = get_object_or_404(shop, slug=post,
                                        publish__year=year,
                                        publish__month=month,
                                        publish__day=day)
        return render(request,'shop/post/detali.html',{'post': post})


# def main_list(request):
#         post1 = shop.objects.all()
#         return render(request,'shop/post/index.html', {'posts': post1})


      
