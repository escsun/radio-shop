from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import PasswordResetForm
from .forms import MyAuthenticationForm, MyUserCreationForm, UserActivationForm
from .models import User, Profile
from .utils import send_mail_function


# Create your views here.

@csrf_protect
def user_login(request):
    if request.POST:
        form = MyAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
    else:
        form = MyAuthenticationForm()
    return render(request, 'account-login.html', {'form': form})


@csrf_protect
def user_register(request):
    if request.POST:
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save()
            instance = Profile.objects.get(user__email=email)
            code = request.build_absolute_uri(reverse("user_activation_confirm", args=(instance.activation_key,)))
            send_mail_function(email,
                               {"code": code, "username": instance.user.username},
                               subject='Регистрация на сайте',
                               template_html='mail/account_activate_mail.html',
                               template_text='mail/account_activate_mail.txt')
            messages.success(request, "Вам отправлено письмо с инструкциями по активации аккаунта.")
            return HttpResponseRedirect(reverse('register'))
    else:
        form = MyUserCreationForm()
    return render(request, 'account-register.html', {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


@csrf_protect
def user_activation(request):
    if request.POST:
        form = UserActivationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                instance = Profile.objects.get(user__email=email)
                code = request.build_absolute_uri(reverse("user_activation_confirm", args=(instance.activation_key,)))
                send_mail_function(email,
                                   {"code": code, "username": instance.user.username},
                                   subject='Активация аккаунта',
                                   template_html='mail/email_activate.html',
                                   template_text='mail/email_activate.txt')
                messages.success(request, "Вам отправлено письмо с кодом активации аккаунта.")
            except ObjectDoesNotExist:
                messages.warning(request, "Сообщение c кодом активации аккаунта не было отправлено.")
        return HttpResponseRedirect(reverse('user_activation'))
    else:
        form = UserActivationForm()
    return render(request, 'account-activation.html', {"form": form})


def user_activation_done(request):
    return render(request, 'account-activation-done.html')


def user_activation_confirm(request, key):
    instance = get_object_or_404(Profile, activation_key=key)
    if instance:
        user = User.objects.get(id=instance.user_id)
        user.is_active = True
        user.save()
        instance.delete()
    return HttpResponseRedirect(reverse('user_activation_done'))


@csrf_protect
def user_password_reset(request,
                        template_name='account-password-reset.html',
                        email_template_name='registration/password_reset_email.html',
                        subject_template_name='registration/password_reset_subject.txt',
                        password_reset_form=PasswordResetForm,
                        token_generator=default_token_generator,
                        from_email=None,
                        html_email_template_name=None):
    if request.method == "POST":
        form = password_reset_form(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': token_generator,
                'from_email': from_email,
                'email_template_name': email_template_name,
                'subject_template_name': subject_template_name,
                'request': request,
                'html_email_template_name': html_email_template_name,
            }

            email = form.cleaned_data['email']
            try:
                instance = User.objects.get(email=email, is_active=True)
                messages.success(request, "На вашу электронную почту было отправлено письмо с инструкцией по смене пароля")
            except ObjectDoesNotExist:
                messages.warning(request, "Этот аккаунт не активирован или отключен")
            form.save(**opts)
            return HttpResponseRedirect(reverse('password_reset'))
    else:
        form = password_reset_form()
    return render(request, template_name, {"form": form})
