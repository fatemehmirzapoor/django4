from django.contrib import admin
# Register your models here.
from .models import Main

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author')
    list_filter = ('author',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
   
