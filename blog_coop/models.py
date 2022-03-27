from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, help_text='Введите имя заголовка', verbose_name='Имя заголовка')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField(help_text='содержимое', verbose_name='Введите текст')

    def __str__(self):
        return self.title
