# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class shop(models.Model):
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='Shop_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    price = models.IntegerField(default=1000)
    Discounted_price = models.IntegerField(default=1000)
    count = models.IntegerField(default=1)

    # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('shop:post_detail',
                         args=[self.publish.year,self.publish.month,self.publish.day, self.slug])
    

class Comment(models.Model):
    shop = models.ForeignKey(shop,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return f'Comment by {self.name} on {self.shop}'