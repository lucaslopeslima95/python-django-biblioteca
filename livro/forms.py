from django import forms
from django.forms import ModelForm
from .models import livro as Livro

class LivroForm(ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Titulo","class": "form-control"}))
    autor = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Autor","class": "form-control"}))
    descricao = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Descrição","class": "form-control"}))
    isbn = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "ISBN",
        "class": "form-control",
        
        'type':'number',
        'maxlength': 17}))
    esta_disponivel = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={}),initial=True)
    class Meta:
        model = Livro
        fields = ['titulo','autor','descricao','isbn','esta_disponivel']
    
class BuscarLivroForm(forms.Form):
    titulo = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Buscar Por Titulo","class": "form-control"}))