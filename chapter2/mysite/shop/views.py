# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import shop,Comment
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .forms import EmailPostForm,CommentForm
from django.core.mail import send_mail
from taggit.models import Tag



def shop_list(request,tag_slug=None):
        object_list = shop.objects.all()
        tag = None
        if tag_slug:
                tag = get_object_or_404(Tag, slug=tag_slug)
                object_list = object_list.filter(tags__in=[tag])
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
                        'posts': posts,'tag': tag})

def shop_detail(request, year, month, day, post):
        post = get_object_or_404(shop, slug=post,
                                        publish__year=year,
                                        publish__month=month,
                                        publish__day=day)


        comments = post.comments.filter(active=True)
        new_comment = None

        if request.method == 'POST':
        # A comment was posted
                comment_form = CommentForm(data=request.POST)
                if comment_form.is_valid():
                        # Create Comment object but don't save to database yet
                        new_comment = comment_form.save(commit=False)
                        # Assign the current post to the comment
                        new_comment.shop = post
                        # Save the comment to the database
                        new_comment.save()
        else:
                comment_form = CommentForm()
        return render(request,'shop/post/detali.html',{'post': post,'comments': comments,'new_comment': new_comment,'comment_form': comment_form})


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






      
