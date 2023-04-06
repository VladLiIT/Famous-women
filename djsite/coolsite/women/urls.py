from django.urls import path, re_path

from .views import *

urlpatterns = [
  
    path('', WomenHome.as_view(), name='home'),                                         # прописали все маршруты текущего приложения  http://127.0.0.1:8000/
    path('about/', about, name='about'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
] 

    