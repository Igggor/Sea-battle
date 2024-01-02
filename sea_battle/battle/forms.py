from django import forms


class Registration(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_double = forms.CharField(widget=forms.PasswordInput())


class Login(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
