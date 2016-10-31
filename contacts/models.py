from django.db import models
from django.template.defaultfilters import truncatechars


class Contacts(models.Model):
    """"Модель контактов - Форма обратной связи"""
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Электронная почта")
    message = models.TextField(verbose_name="Сообщение")
    date = models.DateTimeField(verbose_name="Дата и время", auto_now=True, auto_created=True)

    class Meta:
        verbose_name_plural = "Сообщения"
        verbose_name = "Сообщение"

    def __str__(self):
        return self.message

    def short_message(self):
        return truncatechars(self.message, 80)
    short_message.short_description = "Короткое сообщение"