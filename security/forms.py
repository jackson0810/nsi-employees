from django import forms
from django.forms import ModelForm
from django.db.models import Q

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
        password_required = kwargs.get('password_required', False)

        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].error_messages = {'required': 'Email is required.'}
        self.fields['password'].widget = forms.PasswordInput(attrs={'maxlength': 100})
        self.fields['password'].required = password_required

    class Meta(object):
        model = CustomUser
        fields = ['email', 'password']

    def clean(self):
        cleaned_data = super(CustomUserForm, self).clean()
        email = self.cleaned_data.get('email').lower()

        if email:
            email_found = CustomUser.objects.filter(email=email)

            if email_found:
                self._errors['email'] = self.error_class([u'Email is already in use.'])
                del cleaned_data['email']

        return cleaned_data
