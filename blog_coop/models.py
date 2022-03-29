from django.db import models
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, help_text='Введите имя заголовка', verbose_name='Имя заголовка')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField(help_text='содержимое', verbose_name='Введите текст')

    def __str__(self):
        return self.title

    # Настраивает редирект данной модели - первый арг куда редирект, второй с какими параметрами,
    # юзать вместо {% url /post_details/<int:pk>/ %}. Нужен только с манипуляциями над БД, в остальном обычное url
    # при удалении views.py -> succsess_url = reverse_lazy('') для исполнения в конце
    def get_absolute_url(self):
        return reverse('post_details', args=[str(self.id)])
