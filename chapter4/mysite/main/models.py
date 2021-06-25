# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Main(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='Main_posts')
  
