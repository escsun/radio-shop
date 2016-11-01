from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from django.contrib.messages import get_messages

from .forms import ContactsForm


class ContactsFormTest(TestCase):
    """Тесты для формы"""

    def test_contact_form_valid(self):
        """Стандартная проверка"""
        form = ContactsForm(data={"name": "test name", "email": "test@mail.com", "message": "this is test message"})
        self.assertTrue(form.is_valid())

    def test_contact_form_message_invalid(self):
        """Пустое сообщение не должно быть"""
        form = ContactsForm(data={"name": "test name", "email": "test@mail.com", "message": ""})
        self.assertFalse(form.is_valid())

    def test_contact_form_email_invalid(self):
        """Неправильный email"""
        form = ContactsForm(data={"name": "test name", "email": "test", "message": "this is test message"})
        self.assertFalse(form.is_valid())


class ContactsViewTest(TestCase):
    """Тесты для проверки на сайте"""

    def test_contacts_page_valid(self):
        """Проверяем доступность и шаблон"""
        response = self.client.get(reverse('contacts'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, "contacts.html")

    def test_contacts_post_valid(self):
        """Проверяем запрос post"""
        client = Client(enforce_csrf_checks=True)
        response = client.post(reverse('contacts'))
        self.assertTrue(response.status_code, 200)

    def test_contact_messages_valid(self):
        # """Проверяем получение сообщения после отправки сообщения"""
        response = self.client.post(reverse('contacts'), data={"name": "test name", "email": "test@mail.com", "message": "this is test message"}, follow=True)
        messages = list(response.context["messages"])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Ваше сообщение было отправлено!")