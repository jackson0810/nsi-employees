from django import forms
from django.forms import ModelForm

from shared.forms import RadioSelectInline
from security.models import CustomUser


class LoginForm(forms.Form):
    email = forms.CharField(error_messages={'required': 'Please enter your email address.'})
    password = forms.CharField(error_messages={'required': 'Please enter your password.'},
                               widget=forms.PasswordInput(attrs={'maxlength': 100}))


class CreatePasswordForm(forms.Form):
    password = forms.CharField(error_messages={'required': 'Please enter your email address.'},
                               widget=forms.PasswordInput(attrs={'maxlength': 100}))
    password_verify = forms.CharField(widget=forms.PasswordInput(attrs={'maxlength': 100}))


class ResetPasswordForm(forms.Form):
    email = forms.CharField(error_messages={'required': 'Please enter your email address.'})


class CustomUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)

        account_types = [(1, 'Administrator'), (2, 'General User')]
        bool_choices = ((True, 'Yes'), (False, 'No'))

        self.fields['mobile_phone'].required = False
        self.fields['email'].error_messages = {'required': 'Email is required.'}
        self.fields['account_type'] = forms.ChoiceField(choices=account_types, widget=RadioSelectInline)
        self.fields['is_active'] = forms.ChoiceField(choices=bool_choices, widget=RadioSelectInline)

    class Meta(object):
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'office_phone', 'mobile_phone', 'account_type', 'is_active']
