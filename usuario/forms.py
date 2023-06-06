from django import forms

class authForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username","class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Senha","class": "form-control"}))

class registerForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username","class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email","class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password","class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password check","class": "form-control"}))

class update_User_Form(forms.Form):
    id = forms.CharField(widget=forms.TextInput(attrs={"type":"hidden","class":"form-control","id":"input_old_id"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username","class": "form-control","id":"input_username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email","class": "form-control","id":"input_email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password","class": "form-control"}))