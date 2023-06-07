from django import forms

class registerBookForm(forms.Form):
    titulo = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Titulo","class": "form-control"}))
    authors = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Autor","class": "form-control"}))
    descricao = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Descrição","class": "form-control"}))
    isbn = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "ISBN","class": "form-control"}))
    esta_disponivel = forms.BooleanField(required=False)
    
class searchBookForm(forms.Form):
    titulo = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Buscar Por Titulo","class": "form-control"}))