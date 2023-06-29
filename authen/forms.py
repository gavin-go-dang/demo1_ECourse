from django import forms
import copy
from .models import User
from django.contrib.auth.models import Group


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30)
    full_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    type = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is exist")

        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is exist")

    def create_user(self):
        self.cleaned_data["is_staff"] = self.cleaned_data["type"] == "teacher"

        user = User.objects.create_user(**self.cleaned_data)
        teacher_group = Group.objects.get(name="teacher")
        teacher_group.user_set.add(user)
