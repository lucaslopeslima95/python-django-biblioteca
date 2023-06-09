from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class authForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username","class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Senha","class": "form-control"}))

class registerForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username","class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email","class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password","class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password check","class": "form-control"}))
    
class updateForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username","class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email","class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password","class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Repeat Password","class": "form-control"}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


