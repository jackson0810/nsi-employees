import re
import datetime

from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.db import transaction

from security.forms import LoginForm, CreatePasswordForm, ResetPasswordForm
from shared.utilities import random_password_generator

from .backends import AuthenticationFailedException

User = get_user_model()


def login_form(request, template_name='login.html'):
    try:
        with transaction.atomic():
            has_error = False
            authentication_error = None

            if request.method == 'POST':
                form = LoginForm(request.POST)

                email = request.POST['email'].lower()
                password = request.POST['password']

                if form.is_valid():
                    user = authenticate(email=email, password=password)

                    if user:
                        if user.is_active:
                            # check to see if the user has reset their password and if the time period has expired
                            if user.password_reset:
                                account_time_delta = user.dt_password_reset + datetime.timedelta(
                                    hours=settings.TEMP_PASSWORD_EXPIRES)

                                if datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") >= account_time_delta.strftime("%Y-%m-%d %H:%M:%S"):
                                    messages.error(request, 'Your temporary password has expired.  You must request a new one.')
                                    return redirect('reset_password')

                            if user.password_reset:
                                return redirect('create_new_password', user.administrative_user.administrative_uuid)

                            user.backend = settings.AUTHENTICATION_BACKENDS[0]

                            login(request, user)

                            # record the date/time the user last logged in.
                            user.dt_last_login = datetime.datetime.now()
                            user.save()

                            if user.administrative_user.office == 'GAO' and user.administrative_user.account_type.id == 2:
                                return redirect('conflict_reviewer')
                            else:
                                if not user.administrative_user.office == 'OPR':
                                    return redirect('dashboard')
                                else:
                                    return redirect('reports')
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
    return redirect('login')


def create_new_password(request, user_id, template_name='createNewPassword.html'):
    used_temp_password_error = False
    password_error = False

    if request.method == 'POST':
        form = CreatePasswordForm(request.POST)

        password = request.POST.get('password')
        password_verify = request.POST.get('password_verify')

        user = User.objects.select_related('administrative_user__account_type').get(
            administrative_user__administrative_uuid=user_id)

        if not re.match(settings.PASSWORD_REGEX, password):
            messages.error(request, "Your password does not meet the complexity requirements.")
            return redirect('create_new_password', user.administrative_user.administrative_uuid)

        if user.check_password(password):
            used_temp_password_error = True
        elif password or password_verify:
            if (not password or not password_verify) or password != password_verify:
                password_error = True

        # in error state: send to form for corrections.
        if used_temp_password_error or password_error:
            messages.error(request, settings.GENERIC_ERROR)
            return render(request, template_name, locals())

        if form.is_valid():
            user.set_password(password)
            user.password_reset = False
            user.dt_password_reset = None
            user.dt_last_login = datetime.datetime.now()
            user.save()

            user.backend = settings.AUTHENTICATION_BACKENDS[0]

            login(request, user)

            if user.administrative_user.office == 'GAO' and user.administrative_user.account_type.id == 2:
                return redirect('conflict_reviewer')
            else:
                if not user.administrative_user.office == 'OPR':
                    return redirect('dashboard')
                else:
                    return redirect('reports')

    else:
        form = CreatePasswordForm()

    return render(request, template_name, locals())


def reset_password(request, template_name='resetPassword.html'):
    email_body_plain = ''
    temp_expire = settings.TEMP_PASSWORD_EXPIRES
    has_error = False

    # if request.method == 'POST':
    #     try:
    #         form = ResetPasswordForm(request.POST)
    #
    #         if form.is_valid():
    #             # Random string 10 characters long based on upper, lower, digits and special characters
    #             new_password = random_password_generator(size=10)
    #
    #             email = request.POST['email']
    #
    #             user = User.objects.get_pgp_annotated().get(account_type=4, email__decrypted=email)
    #             user.set_password(new_password)
    #             user.password_reset = True
    #             user.dt_password_reset = datetime.datetime.now()
    #             user.save()
    #
    #             email_template_data = AutomaticEmailTemplate.objects.get(
    #                 email_template_uuid='ff3a8713-35a8-4a2c-9e6d-823e77f14f36')
    #
    #             email_subject = email_template_data.email_template_subject
    #             email_body_html = email_template_data.email_content.replace("#temporary_password#", new_password)
    #             email_body_html = email_body_html.replace("#application_url#", settings.APP_URL)
    #             email_body_html = email_body_html.replace("#password_expire#", str(temp_expire))
    #
    #             email = EmailMultiAlternatives(email_subject, '', settings.SYSTEM_EMAIL_ADDRESS, [email])
    #             email.attach_alternative(email_body_html, "text/html")
    #
    #             email.send(fail_silently=False)
    #
    #             messages.success(request, """Your password reset has been processed. You will receive an email
    #                                       containing a temporary password.""")
    #
    #             return redirect('login')
    #         else:
    #             # form is not valid
    #             messages.error(request, settings.GENERIC_ERROR)
    #     except User.DoesNotExist:
    #         messages.error(request, 'A password reset request could not be processed for this email address.')
    #         return redirect('reset_password')
    # else:
    #     form = ResetPasswordForm()

    return render(request, template_name, {'form': form})
