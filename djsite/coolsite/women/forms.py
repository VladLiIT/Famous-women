from django import forms
from .models import *
from django.core.exceptions import ValidationError


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):        
        super().__init__(*args, **kwargs)                                     #  Вызов конструктора базового класса
        self.fields['cat'].empty_label = "Категория не выбрана"               #  Присваиваем вместо пустой строки в категории "Категория не выбрана" 


    class Meta: 
        model = Women                                                         #  Взаимодействие model c class Women
        # fields = '__all__'                                                  #  Какие поля отобразить в форме | __all__ показывает все поля кроме тех что заполняются автоматом
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 70, 'rows': 10}),
        }


    def clean_title(self):                    #  Валидация для заголовка 
        title =self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError("Длина превышает 200 символов")
        return title