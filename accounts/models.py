from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail


class User(AbstractBaseUser, PermissionsMixin):
    """
        An abstract base class implementing a fully featured User model with
        admin-compliant permissions.

        Username, password and email are required. Other fields are optional.
        """
    username = models.CharField(_('username'), max_length=30, unique=True,
                                help_text=_('Требуется, не больше 30 символов или меньше, '
                                            'латинские буквы, числа, знаки подчеркивания и дефис.'),
                                validators=[
                                    validators.RegexValidator(r'^[A-z0-9_-]+$',
                                                              ('Логин может содержать только латинские буквы, '
                                                               'числа, знаки подчеркивания и дефис. '
                                                               'Ограничения не больше 30 символов или меньше.'), 'invalid'),
                                ],
                                error_messages={
                                    'unique': _("A user with that username already exists."),
                                })
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True,
                              error_messages={
                                  'unique': _("Пользователь с таким электронным адресом уже существует."),
                              })
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = False

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Profile(models.Model):
    user = models.ForeignKey(User, related_name="profile")
    activation_key = models.CharField(max_length=64)
    # key_expires = models.DateTimeField()
