from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.admin import Group as AuthGroup
from .models import User


class Group(AuthGroup):
    class Meta:
        proxy = True
        app_label = "accounts"
        verbose_name_plural = "Группы"
        verbose_name = "Группа"


class MyUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets
    list_display = ('username', 'email', 'is_staff', 'is_active')

    # fieldsets = UserAdmin.fieldsets + (
    #         (None, {'fields': ('some_extra_data',)}),
    # )

admin.site.unregister(AuthGroup)
admin.site.register(User, MyUserAdmin)
admin.site.register(Group, GroupAdmin)
