from django import forms

class ClienteForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Nome","class": "form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Email","class": "form-control"}))
    data_nascimento = forms.DateField()
    endereco = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Endereço","class": "form-control"}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Telefone","class": "form-control"}))

class BuscaClienteNomeForm(forms.Form):
    nome_cliente = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Informe o nome do Cliente","class": "form-control"}))