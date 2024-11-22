# from typing import Any


from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# from users.models import Profie, User

from .forms import RegisterForm, LoginForm

# Create your views here.
class RegisterView(generic.CreateView):
    template_name = 'pages/user/login.html'
    form_class = RegisterForm
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.save()
        login(self.request,user)
        return redirect('index')
    
def logout_user(request):
    logout(request)
    return redirect('index')
    

class UserLoginView(LoginView):
    template_name = 'pages/user/login.html'
    form_class = LoginForm

    def get_success_url(self) -> str:
        return  reverse_lazy('index')
    
# class Profile(generic.DetailView):
#     template_name = 'page/profile.html'
#     model = User
#     context_object_name = 'user'
    
    
    
#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         title = f'Профиль {context["user"].username}'
#         context['profile'] = Profie.objects.get(user_id=context["user"].id)
#         context['title'] = title
#         return context