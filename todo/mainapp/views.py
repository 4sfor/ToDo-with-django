from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from .forms import LoginUserForm
from .models import Task
from django.contrib.auth.views import LoginView
# Create your views here.

def index(request):
    taskList=Task.objects.all()
    return render(request,'mainapp/index.html',{'taskList': taskList})

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'mainapp/registration/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')
