from django import forms


class UpdateUserInfoForm(forms.Form):
    full_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    # date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
