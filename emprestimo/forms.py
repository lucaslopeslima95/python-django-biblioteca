from django import forms
from django.forms import ModelForm
from .models import Emprestimo
from .models import Status_emprestimo
from clientes.models import Cliente
from livro.models import livro as Livro


class RegistroEmprestimoForm(ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    livro = forms.ModelChoiceField(queryset=Livro.objects.all())
    data_emprestimo = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Selecione uma data', 'autocomplete': 'off','value':''}))
    data_devolucao = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Selecione uma data', 'autocomplete': 'off','value':''}))
    status_emprestimo = forms.ChoiceField(choices=Status_emprestimo.choices)
    class Meta:
        model = Emprestimo
        fields = ['cliente','livro','data_emprestimo','data_devolucao','status_emprestimo']
