from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.messages import get_messages

from .forms import ContactsForm


@csrf_protect
def contacts(request):
    if request.POST:
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваше сообщение было отправлено!")
            return HttpResponseRedirect(reverse('contacts'))
    else:
        form = ContactsForm()
    return render(request, 'contacts.html', {'form': form})
