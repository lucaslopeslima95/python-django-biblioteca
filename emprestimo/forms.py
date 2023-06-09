from django import forms
from django.forms import ModelForm
from .models import emprestimo
from clientes.models import Cliente
from livro.models import livro as Livro

class RegistroEmprestimoForm(ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    livro = forms.ModelChoiceField(queryset=Livro.objects.all())
    data_emprestimo = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Selecione uma data', 'autocomplete': 'off','value':''}))
    data_devolucao = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Selecione uma data', 'autocomplete': 'off','value':''}))
    situacao = forms.BooleanField(label="Concluido:")
    class Meta:
        model = emprestimo
        fields = ['cliente','livro','data_emprestimo','data_devolucao','situacao']
