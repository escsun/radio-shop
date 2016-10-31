from django import forms
from .models import Contacts


class ContactsForm(forms.ModelForm):
    """Форма обратной связи"""
    class Meta:
        model = Contacts
        fields = ('name', 'email', 'message')
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6, 'style': 'resize: vertical'})
        }

    def clean_message(self):
        """Проверяет количество слов в сообщение"""
        message = self.cleaned_data['message']
        num_words = len(message.split())
        # Количество слов
        number_of_words = 4
        if num_words < number_of_words:
            raise forms.ValidationError("Недостаточно слов, необходимо не меньше чем %d слова." % number_of_words)
        return message