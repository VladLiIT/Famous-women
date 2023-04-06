from django.contrib import admin
from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')      #  Заголовки в моделях admin django
    list_display_links = ('id', 'title')                                        
    search_fields = ('title', 'content')                                        #  Поиск по в admin django
    list_editable = ('is_published',)                                           #  Поле публикации сделать редактируемым в admin django
    list_filter = ('is_published', 'time_create')                               #  Фильтр по публикации статей в admin django
    prepopulated_fields = {"slug": ("title",)}        #  Автозаполнение Slug в admin django  


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')                     #  Заголовки в моделях admin django
    list_display_links = ('id', 'name')                                        
    search_fields = ('name',)                         #  Ставим запятую в конце т.к это кортеж
    prepopulated_fields = {"slug": ("name",)}         #  Автозаполнение Slug в admin django  

admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
