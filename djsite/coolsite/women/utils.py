from .models import *
from django.db.models import Count

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'},
]


class DataMixin:
    paginate_by = 3                                            #  Кол-во элементов на 1-й странице
    
    def get_user_context(self, **kwargs):                       #  Создает контекст для шаблона  f.e template_name --> 'women/index.html'
        #  Формируется начальный словарь из именованных параметров которые были переданы функцией get_usr_context
        context = kwargs                                        #  Формирование списка категорий
        cats = Category.objects.annotate(Count('women'))        #  Не отображать рубрику(и) в которых отсутствует запись статья
        user_menu = menu.copy()                                 #  Создает копию словаря 'menu' с сохраняем ее в переменной 'user_menu'
        #  Если пользователь не авторизован то из списка удаляем 1-ый индекс т.е {'title': "Добавить статью", 'url_name': 'add_page'},
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu                             #  Передает ссылку на 'menu'
        context['cats'] = cats                                  #  Прописывает контекст для рубрик
        
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
        