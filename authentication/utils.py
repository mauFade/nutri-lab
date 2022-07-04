import re
from django.contrib import messages
from django.contrib.messages import constants

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