from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import MyAuthenticationForm, MyUserCreationForm, UserActivationForm
from .models import User, Profile
from .utils import send_mail_function
# Create your views here.


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

