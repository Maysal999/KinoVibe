from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    # password1 = forms.CharField(
    #     max_length=100,widget=forms.PasswordInput(attrs={"class" : "input-box"}),label='пароль'   )
    # password2 = forms.CharField(
    #     max_length=100,widget=forms.PasswordInput(attrs={"class" : "input-box"}),label=' подверждения пароль'   )
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        # widgets = {
        #     'username' : forms.TextInput(attrs={'class' : 'input-box'}),
        #     'email' : forms.TextInput(attrs={'class' : 'input-box'}),

        # }

class LoginForm(AuthenticationForm):
    class Meta:
        model =User
        fields = ('username','password')