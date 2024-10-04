from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import RegisterForm, LoginForm

# Create your views here.
class RegisterView(generic.CreateView):
    template_name = 'pages/login.html'
    form_class = RegisterForm
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.save()
        login(self.request,user)

def logout_user(request):
    logout(request)
    return redirect('index')
    

class UserLoginView(LoginView):
    template_name = 'pages/login.html'
    form_class = LoginForm

    def get_success_url(self) -> str:
        return  reverse_lazy('index')