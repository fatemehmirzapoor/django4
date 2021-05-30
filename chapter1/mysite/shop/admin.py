from django.contrib import admin

# Register your models here.
from .models import shop

@admin.register(shop)
class shopAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user', 'publish','price','Discounted_price')
    list_filter = ('created', 'publish', 'user')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('user',)
    date_hierarchy = 'publish'
    ordering = ('publish',)
    list_editable = ('price','Discounted_price')
