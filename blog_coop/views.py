from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy # # редирект выполнится всегда в конце при полном завершении исполнения алгоритма
# Create your views here.


class IndexAsView(ListView): #Для отображения обьектов из колонки
    model = Post
    template_name = 'index.html'


class BlogDetailView(DetailView): # Для детального отображения информации о обьекте
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView): #Создание через форму, при сабмите - добавление в базу
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body'] # В создании поста будут указаны три поля из базы данных,
    # в которые при сабмите будут добавлена новая инфа


class BlogEditView(UpdateView): # Редактирование ранее созданных данных
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    field = ['title']
    success_url = reverse_lazy('index') # При удалении из базы по pk и редирект
