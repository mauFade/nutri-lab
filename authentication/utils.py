import re
from django.contrib import messages
from django.contrib.messages import constants

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def password_is_valid(request, password, confirm_password):
    if len(password) < 6:
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter 6 ou mais caractertes')
        return False

    if not password == confirm_password:
        messages.add_message(request, constants.ERROR, 'As senhas não coincidem!')
        return False
    
    if not re.search('[A-Z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras maiúsculas')
        return False

    if not re.search('[a-z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras minúsculas')
        return False

    if not re.search('[1-9]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contém números')
        return False

    return True

def fields_are_blank(request, name, email, password):
    if len(name) == 0:
        messages.add_message(request, constants.ERROR, "Você deve enviar um nome")
        return False
    if len(email) == 0:
        messages.add_message(request, constants.ERROR, "Você deve enviar um email")
        return False
    if len(password) == 0:
        messages.add_message(request, constants.ERROR, "Você deve enviar uma senha")
        return False

    return True

def email_html(path_template: str, subject: str, to: list, **kwargs) -> dict:
    html_content = render_to_string(path_template, kwargs)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, to)

    email.attach_alternative(html_content, "text/html")
    email.send()
    return {"status": 1}