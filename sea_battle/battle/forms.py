from django import forms


class Autor(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_double = forms.CharField(widget=forms.PasswordInput())
