from django import template
from women.models import *

register = template.Library()                                #  Регистрация шаблонных тегов

@register.simple_tag(name='getcats')                         #  Связка метода get_categories с тегом при помощи декоратора
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('women/list_categories.html')                
def show_categories(sort=None, cat_selected=0):              #  Возвращает полноценную html страницу
    if not sort:
        cats = Category.objects.all()                        #  Читает все категории из стр. Категории
    else:
        cats = Category.objects.order_by(sort)
    
    return {"cats": cats, "cat_selected": cat_selected}      #  Возвращает словарь 