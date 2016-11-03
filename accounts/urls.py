from django.conf.urls import url
from .views import user_login, user_register, user_logout, user_activation, user_activation_confirm, user_activation_done
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', user_login, name='login'),
    url(r'^register/$', user_register, name='register'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^activation/$', user_activation, name='user_activation'),
    url(r'^activation/done/$', user_activation_done, name="user_activation_done"),
    url(r'^activation/(?P<key>\w+)/$', user_activation_confirm, name="user_activation_confirm"),

    url(r'^password_reset/$',
        auth_views.password_reset,
        {"template_name": "account-password-reset.html"},
        name='password_reset'),

    url(r'^password_reset/done/$',
        auth_views.password_reset_done,
        {"template_name": "account-password-reset-done.html"},
        name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {"template_name": "account-password-reset-confirm.html"},
        name='password_reset_confirm'),

    url(r'^reset/done/$',
        auth_views.password_reset_complete,
        {"template_name": "account-password-reset-complete.html"},
        name='password_reset_complete'),

    url(r'^password_change/$',
        auth_views.password_change,
        {"template_name": "account-password-change.html"},
        name='password_change'),

    url(r'^password_change/done/$',
        auth_views.password_change_done,
        {"template_name": "account-password-change-done.html"},
        name='password_change_done'),
]