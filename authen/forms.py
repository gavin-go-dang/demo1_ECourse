from django import forms
from .models import User


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30)
    fullname = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    type = forms.CharField(max_length=9)

    def clean(self):
        cleaned_data = super().clean()

        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("confirm_password")

        if password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        username = cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is exist")

        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is exist")
