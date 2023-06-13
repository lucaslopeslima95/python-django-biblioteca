from django import forms
from django.forms import ModelForm
from .models import Emprestimo
from .models import Status_emprestimo
from clientes.models import Cliente
from livro.models import livro as Livro
import datetime


class RegistroEmprestimoForm(ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.filter(pode_fazer_emprestimo=True),widget=forms.Select(attrs={'class': 'form-control'}))
    livro = forms.ModelChoiceField(queryset=Livro.objects.filter(esta_disponivel=True),widget=forms.Select(attrs={'class': 'form-control'}))
    data_emprestimo = forms.DateField(initial=datetime.date.today ,widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Selecione uma data', 'autocomplete': 'off','readonly':True}))
    data_devolucao = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Selecione uma data', 'autocomplete': 'off','value':''}))
    status_emprestimo = forms.ChoiceField(
        choices=Status_emprestimo.choices,
        widget=forms.Select(
            attrs={'class': 'form-control ','readonly':True}))
    class Meta:
        model = Emprestimo
        fields = ['cliente','livro','data_emprestimo','data_devolucao','status_emprestimo']
