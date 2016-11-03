from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string


def send_mail_function(email_to, context, subject, template_text="mail/email.txt", template_html="mail/email.html"):
    context = Context(context)
    template_text = render_to_string(template_text, context)
    template_html = render_to_string(template_html, context)

    email = EmailMultiAlternatives(subject=subject, body=template_text)
    email.attach_alternative(template_html, "text/html")
    email.to = [email_to]
    email.send()

