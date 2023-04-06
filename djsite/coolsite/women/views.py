from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .forms import *
from .models import *
from .utils import *


class WomenHome(DataMixin, ListView):
    model = Women                                                     #  Отобразить список статей
    template_name = 'women/index.html'                                #  Указать ссылку на шаблон          
    context_object_name = 'posts'                                     #  Указать переменную 'posts'          


    def get_context_data(self, *, object_list=None, **kwargs):        #  Метод формирует динамический и статический контекст
        context = super().get_context_data(**kwargs)                  #  Получение контекста для уже сформированного шаблона
        #  Обращение у get_user_context из utils.py и передает именованный параметр title
        c_def = self.get_user_context(title="Главная страница")
        #  Объединяем 2 словаря в 1: context(на основе class ListView) и c_def(на основе class DataMixin)
        return dict(list(context.items()) + list(c_def.items()))      

    def get_queryset(self):                                           #  Метод позволяющий фильтровать публикации т.е показывать только то что разрешено
        return Women.objects.filter(is_published=True)                #  Показывать только те публикации в которых значение True


# def index(request):
#     posts = Women.objects.all()

#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }

#     return render(request, 'women/index.html', context=context)                           # прописали путь к шаблону index.html в папке women


def about(request):
    contact_list = Women.objects.all()                                 #  Вывод списка женщин
    paginator = Paginator(contact_list, 3)                             #  Вывод 3-х элементов на 1-й стр.

    page_number = request.GET.get('page')                              #  Получить номер текущей стр.
    page_obj = paginator.get_page(page_number)                         #  Список элементов текущей стр.
    return render(request, 'women/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'О сайте'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm                                          #  Указывает на класс формы AddPostForm
    template_name = 'women/addpage.html'                              #  Подключает для работы нужный нам шаблон
    #  Перенаправление адреса маршрута при добавлении новой статьи 
    #  'home' это ссылка на главную страницу
    # reverse_lazy выполняет построение маршрута только тогда когда это неоходимо в отличии от reverse
    success_url = reverse_lazy('home')    
    #  Указывает на адрес перенаправления для незарегистр. пользователей на главную страницу           
    login_url = reverse_lazy('home')    
    raise_exception = True                                            #  Доступ на сайт запрещен для незарегистр. пользователей 


    def get_context_data(self, *, object_list=None, **kwargs):        #  Метод формирует динамический и статический контекст
        context = super().get_context_data(**kwargs)                  #  Получение контекста для уже сформированного шаблона 
        #  Обращение у get_user_context из utils.py и передает именованный параметр title
        c_def = self.get_user_context(title="Добавление статьи")  
        #  Объединяем 2 словаря в 1: context(на основе class ListView) и c_def(на основе class DataMixin)
        return dict(list(context.items()) + list(c_def.items())) 


# def add_page(request):
#     if request.method == 'POST':                               #  Если данные были раннее введены при авторизации
#         form = AddPostForm(request.POST, request.FILES)        #  Хранение всех заполненных данных требуемых для ввода в поле ввода
#         if form.is_valid():                                    #  Проверка на корректность заполненных данных        
#             form.save()                                        #  Добавление новой записи в БД
#             return redirect('home')                            #  Если добавление прошло успешно, то добавляем его на главную страницу
#     else:                           
#         form = AddPostForm()                                   #  Формирование пустой формы
    
#     return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
    
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }

#     return render(request, 'women/post.html', context=context)


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'                  #  Using variable post_slug from urls.py
    context_object_name = 'post'                  #  Указать переменную 'post'     

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #  Обращение у get_user_context из utils.py и формирует заголовок post
        c_def = self.get_user_context(title=context['post'])  
        #  Объединяем 2 словаря в 1: context(на основе class ListView) и c_def(на основе class DataMixin)
        return dict(list(context.items()) + list(c_def.items())) 
    

class WomenCategory(DataMixin, ListView):
    model = Women                                 #  Отобразить список статей
    template_name = 'women/index.html'            #  Указать ссылку на шаблон          
    context_object_name = 'posts'                 #  Указать переменную 'posts'          
    allow_empty = False

    def get_queryset(self):                                                                   #  Метод позволяющий фильтровать публикации т.е показывать только то что разрешено
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)     #  Показывать только те публикации в которых значение True

    def get_context_data(self, *, object_list=None, **kwargs):                                  
        context = super().get_context_data(**kwargs)                                          #  Фрмирования контекста данных имеющиеся в род. классе ListView
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items())) 


# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)

#     if len(posts) == 0:
#         raise Http404()

#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': "Отображение по рубрикам",
#         'cat_selected': cat_id,
#     }

#     return render(request, 'women/index.html', context=context)