from django.contrib import admin
from django.urls import path, include

#Общий URL для все приложений проекта Blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_coop.urls')), #Считывание всех путей из приложения blog_coop
    path('accounts/', include('django.contrib.auth.urls')) #Авторизация пользователей

]
