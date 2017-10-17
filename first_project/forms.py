from django import forms
from django.core import validators
from first_project.models import User


# def checkForZ(value):
#     if value[0].islower != 'z':
#         raise forms.ValidationError('Name Must be start with z')


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    v_email = forms.EmailField(label='Verified Email: ')
    text = forms.CharField(widget=forms.Textarea)
    botCatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email'].lower()
        v_email = all_clean_data['v_email'].lower()

        if email != v_email:
            raise forms.ValidationError("Email not match")


class NewUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
