from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginUserForm, RegisterUserForm
from .models import Task
from django.contrib.auth.views import LoginView
# Create your views here.

def index(request):
    if request.user.is_authenticated==False:
        return redirect('login')
    current_user = request.user
    unic_dates = Task.objects.filter(user=current_user.id).values_list('deadline',flat=True).distinct()
    deadlinesList={}
    for date in unic_dates:
        task_for_date=Task.objects.filter(deadline=date)
        deadlinesList[str(date)] = task_for_date
    return render(request,'mainapp/index.html',{'deadlinesList': deadlinesList})

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'mainapp/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('index')



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'mainapp/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


def logout_user(request):
    logout(request)
    return redirect('login')