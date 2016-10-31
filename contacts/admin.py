from django.contrib import admin
from .models import Contacts


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'message', 'date', )
    list_display = ('name', 'short_message', 'date',)
    readonly_fields = ('date',)
    search_fields = ('message',)
    date_hierarchy = 'date'
    list_filter = ('date',)
    list_display_links = list_display
    ordering = ('-id',)

# Register your models here.
