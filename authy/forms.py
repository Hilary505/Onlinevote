from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from django.core.validators import EmailValidator


class LoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(min_length=4, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
     class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class loginView(generic.CreateView):
    form_class = UserCreationForm
    Success_url = reverse_lazy("login")
    template_name = "poll/login.html"
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    phone = forms.CharField(max_length=15)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)




