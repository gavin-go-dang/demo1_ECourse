from django import forms
from authen.models import User
from django.db.models import Q


class UpdateUserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["full_name", "email", "date_of_birth"]

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        user_check_count = User.objects.filter(email=email).count()
        if user_check_count > 1:
            raise forms.ValidationError("Email has exist in system")


class CoverImgForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["cover_img"]
