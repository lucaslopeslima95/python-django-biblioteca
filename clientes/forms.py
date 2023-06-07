from django import forms

class authForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Nome","class": "form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Email","class": "form-control"}))
    data_nascimento = forms.DateField()
    endereco = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Endereço","class": "form-control"}))