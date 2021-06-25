from django.contrib import admin
from .models import shop, Comment

# Register your models here.
from .models import shop

@admin.register(shop)
class shopAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user', 'publish','price','Discounted_price','count')
    list_filter = ('title','created', 'publish', 'user','price','count')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('user',)
    date_hierarchy = 'publish'
    ordering = ('publish',)
    list_editable = ('price','Discounted_price')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'shop', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')