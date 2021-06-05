# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import shop
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .forms import EmailPostForm


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

def post_share(request, post_id):
        # Retrieve post by id
        post = get_object_or_404(shop, id=post_id, status='published')
        if request.method == 'POST':
                # Form was submitted
                form = EmailPostForm(request.POST)
                if form.is_valid():
                        # Form fields passed validation
                        cd = form.cleaned_data
                        # ... send email
        else:
                form = EmailPostForm()
        return render(request, 'blog/post/share.html', {'post': post, 'form': form})






      
