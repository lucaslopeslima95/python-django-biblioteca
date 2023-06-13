from django import forms
from django.forms import ModelForm
from .models import Cliente

class ClienteForm(ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Nome","class": "form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Email","class": "form-control"}))
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    endereco = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Endereço","class": "form-control"}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Telefone","class": "form-control"}))
    class Meta:
        model = Cliente
        fields = ['nome','email','data_nascimento','endereco','telefone']

class BuscaClienteNomeForm(forms.Form):
    nome_cliente = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Informe o nome do Cliente","class": "form-control"}))