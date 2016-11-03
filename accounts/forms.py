from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext, ugettext_lazy as _


class MyAuthenticationForm(AuthenticationForm):
    pass


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label=_("Email"))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "email", "password1", "password2"]:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        user = super(MyUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_active = False
        if commit:
            user.save()
        return user


class UserActivationForm(forms.Form):
    email = forms.EmailField(required=True, label=_("Email"))

    # class Meta:
    #     model = User
