# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import shop
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .forms import EmailPostForm
from django.core.mail import send_mail


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
        post = get_object_or_404(shop, id=post_id)
        sent = False

        if request.method == 'POST':
                # Form was submitted
                form = EmailPostForm(request.POST)
                if form.is_valid():
                        # Form fields passed validation
                        cd = form.cleaned_data
                        # ... send email
                        post_url = request.build_absolute_uri(
                        post.get_absolute_url())
                        subject = f"{cd['name']} recommends you read " \
                        f"{post.title}"
                        message = f"Read {post.title} at {post_url}\n\n" \
                        f"{cd['name']}\'s comments: {cd['comments']}"
                        send_mail(subject, message, 'admin@myblog.com',
                        [cd['to']])
                        sent = True
        else:
                form = EmailPostForm()
        return render(request, 'shop/post/share.html', {'post': post, 
                                                                'form': form,'sent': sent})






      