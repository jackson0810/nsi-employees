from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(error_messages = {'required':'Please enter your email address.'})
    password = forms.CharField(error_messages = {'required':'Please enter your password.'}, widget = forms.PasswordInput(attrs={'maxlength':100}))


class CreatePasswordForm(forms.Form):
    password = forms.CharField(error_messages = {'required':'Please enter your email address.'}, widget = forms.PasswordInput(attrs={'maxlength':100}))
    password_verify = forms.CharField(widget = forms.PasswordInput(attrs={'maxlength':100}))


class ResetPasswordForm(forms.Form):
    email = forms.CharField(error_messages = {'required':'Please enter your email address.'})
