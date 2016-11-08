import re
import uuid
from datetime import datetime, timedelta

from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.db import transaction
from django.core.urlresolvers import reverse

from security.forms import LoginForm, CreatePasswordForm, ResetPasswordForm, CustomUserForm
from shared.utilities import random_password_generator, make_uuid

from .backends import AuthenticationFailedException

User = get_user_model()


def login_form(request, template_name='login.html'):
    try:
        with transaction.atomic():
            has_error = False
            authentication_error = None

            if request.user.is_authenticated():
                return redirect('employees:home')

            if request.method == 'POST':
                if request.user.is_authenticated():
                    return redirect(request.POST.get('next', 'employees:home'))

                form = LoginForm(request.POST)

                email = request.POST['email'].lower()
                password = request.POST['password']

                if form.is_valid():
                    user = authenticate(email=email, password=password)

                    if user:
                        if user.is_active:
                            # check to see if the user has reset their password and if the time period has expired
                            if user.password_reset:
                                account_tdelta = user.dt_password_reset + timedelta(
                                    hours=settings.TEMP_PASSWORD_EXPIRES)

                                if datetime.now().strftime("%Y-%m-%d %H:%M:%S") >= account_tdelta.strftime("%Y-%m-%d %H:%M:%S"):
                                    messages.error(request, 'Your temporary password has expired.  You must request a new one.')
                                    return redirect('reset_password')

                            if user.password_reset:
                                return redirect('create_new_password', user.user_uuid)

                            user.backend = settings.AUTHENTICATION_BACKENDS[0]

                            login(request, user)

                            # record the date/time the user last logged in.
                            user.dt_last_login = datetime.now()
                            user.save()

                            return redirect(request.POST.get('next', 'employees:home'))
                        else:
                            has_error = True
                            messages.error(request, 'You do not have an active account.')
                    else:
                        authentication_error = True
                        has_error = True
                        messages.error(request, settings.GENERIC_ERROR)
                else:
                    has_error = True
                    messages.error(request, settings.GENERIC_ERROR)
            else:
                form = LoginForm()
    except AuthenticationFailedException as e:
        messages.error(request, e)
        authentication_error = True
    except Exception as e:
        messages.error(request, 'An error occurred: {} - {}'.format(type(e), e))

    return render(request, template_name, locals())


def user_logout(request):
    logout(request)

    messages.success(request, 'You have logged out.')
    return redirect('security:login')


def create_new_password(request, user_uuid, temporary_password, template_name='createNewPassword.html'):
    password_error = False

    try:
        user = User.objects.get(user_uuid=user_uuid)
    except User.DoesNotExist:
        messages.error(request, 'A password reset could not be processed.')
        return redirect('security:reset_password')

    if request.method == 'POST':
        form = CreatePasswordForm(request.POST)

        password = request.POST.get('password')
        password_verify = request.POST.get('password_verify')

        if not re.match(settings.PASSWORD_REGEX, password):
            messages.error(request, 'Your password does not meet the complexity requirements.')
            password_error = True

            return redirect('security:create_new_password', user_uuid, temporary_password)

        if password != password_verify:
            messages.error(request, 'Your passwords do not match')
            password_error = True

            return redirect('security:create_new_password', user_uuid, temporary_password)

        if form.is_valid():
            user.set_password(password)
            user.password_reset = False
            user.dt_password_reset = None
            user.dt_last_login = datetime.now()
            user.save()

            user.backend = settings.AUTHENTICATION_BACKENDS[0]

            login(request, user)
            messages.success(request, 'Your password has been successfully reset.')

            return redirect('employees:home')
    else:
        if user.check_password(temporary_password):
            # check to see if the time period for use this password has expired.
            account_time_delta = user.dt_password_reset + timedelta(hours=settings.TEMP_PASSWORD_EXPIRES)

            if datetime.now().strftime("%y-%m-%d %H:%M:%S") >= account_time_delta.strftime("%y-%m-%d %H:%M:%S"):
                messages.error(request, 'Your temporary password has expired.  You must request a new one')

                return redirect('security:reset_password')

            form = CreatePasswordForm()
        else:
            messages.error(request, 'The temporary password provided is not valid.  Please try again.')
            return redirect('security:reset_password')

    return render(request, template_name, locals())


def reset_password(request, template_name='resetPassword.html'):
    temp_expire = settings.TEMP_PASSWORD_EXPIRES

    if request.method == 'POST':
        try:
            form = ResetPasswordForm(request.POST)

            if form.is_valid():
                # Random string 10 characters long based on upper, lower, digits and special characters
                new_password = make_uuid()

                email = request.POST['email'].lower()

                user = User.objects.get(email=email)
                user.set_password(new_password)
                user.password_reset = True
                user.dt_password_reset = datetime.now()
                user.save()

                url_pattern = '{}{}'.format(settings.APPLICATION_URL, reverse('security:create_new_password',
                                                                              args=(user.user_uuid, new_password)))

                email_subject = 'NSI Employee Portal Password Reset'
                email_body = """
<p>{first_name}</p>
<p>You have requested a password reset through the NSI Employee Portal. The following link will reset your password.
<a href="{url_pattern}">Please click here to continue.</a></p>
<p>Please keep in mind this temporary password will expire in {password_expire} hours. Upon clicking the link you will
be prompted to create a new password.</p>""".format(first_name=user.first_name, url_pattern=url_pattern,
                                                    password_expire=settings.TEMP_PASSWORD_EXPIRES)

                email = EmailMultiAlternatives(email_subject, '', settings.APPLICATION_EMAIL, [email])
                email.attach_alternative(email_body, "text/html")

                email.send(fail_silently=False)

                messages.success(request, """Your password reset has been processed. You will receive an email
                                          containing a temporary password.""")

                return redirect('security:login')
            else:
                # form is not valid
                messages.error(request, settings.GENERIC_ERROR)
        except User.DoesNotExist:
            messages.error(request, 'A password reset request could not be processed for this email address.')
            return redirect('security:reset_password')
    else:
        form = ResetPasswordForm()

    return render(request, template_name, {'form': form, 'temp_expire': temp_expire})


def team_members(request, user_uuid=None):
    team_member_data = User.objects.all()
    user = None

    if user_uuid:
        user = team_member_data.get(user_uuid=user_uuid)

    if request.method == 'POST':
        if user:
            form = CustomUserForm(request.POST, instance=user)
        else:
            form = CustomUserForm(request.POST)

        if form.is_valid():
            team_member = form.save(commit=False)
            team_member.email = team_member.email.lower()
            team_member.save()

            if not user:
                new_password = make_uuid()
                team_member.set_password(new_password)
                url_pattern = '{}{}'.format(settings.APPLICATION_URL, reverse('security:create_new_password',
                                                                              args=(team_member.user_uuid, new_password)))

                # the employee is new so send them an email with their password.
                email_subject = 'NSI Employee Portal Account Created'

                email_body = """
<p>{first_name}</p>,
<p>An account in the NSI Employee Portal has been created for you.  Please <a href="{url_pattern}">click here</a>
to login.</p>
<p>Please keep in mind this temporary password will expire in {expires} hours. Upon clicking the link you will be
prompted to create a new password.</p>""".format(first_name=team_member.first_name, url_pattern=url_pattern,
                                                 expires=settings.TEMP_PASSWORD_EXPIRES)

                email = EmailMultiAlternatives(email_subject, '', settings.APPLICATION_EMAIL, [team_member.email])
                email.attach_alternative(email_body, "text/html")
                email.send(fail_silently=False)

            messages.success(request, 'The team member data was saved successfully.')
            return redirect('security:team_members')
        else:
            messages.error(request, settings.GENERIC_ERROR)
    else:
        if user:
            form = CustomUserForm(instance=user)
        else:
            form = CustomUserForm()

    return render(request, 'team_members.html', {'form': form, 'team_member_data': team_member_data,
                                                 'user_uuid': user_uuid})
