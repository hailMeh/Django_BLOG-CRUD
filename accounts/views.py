from django.contrib.auth.forms import UserCreationForm #базовая форма для создания учётки
from django.urls import reverse_lazy # редирект выполнится всегда в конце при полном завершении исполнения алгоритма
from django.views import generic
# Create your views here.


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login') #редирект на login, где будет вход под новым аккаунтом


