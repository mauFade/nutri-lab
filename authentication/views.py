from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

from .utils import password_is_valid, fields_are_blank

# Create your views here.
def register(request):
    """"Função para fazer cadastro de um novo usuário"""
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, "register.html")
    elif request.method == "POST":
        name = request.POST.get("usuario")
        email = request.POST.get("email")
        password = request.POST.get("senha")
        confirm_password = request.POST.get("confirmar_senha")

        if not password_is_valid(request, password, confirm_password):
            return redirect("/auth/register")

        if not fields_are_blank(request, name, email, password):
          return redirect("/auth/register")

        try:
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password,
                is_active=False)

            user.save()
            messages.add_message(request, constants.SUCCESS, "Usuário cadastrado com sucesso!")
            return redirect("/auth/login")
        except:
            messages.add_message(request, constants.SUCCESS, "Erro interno do sistema")
            return redirect("/auth/register")
    

def login(request):
    """"Função para fazer login"""
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, "login.html")
    elif request.method == "POST":
        name = request.POST.get("usuario")
        password = request.POST.get("senha")

        user = auth.authenticate(username=name, password=password)

        if not user:
            messages.add_message(request, constants.ERROR, "Usuário não encontrado")
            return redirect("/auth/login")
        else:
            auth.login(request, user)
            return redirect("/")

def logout(request):
    auth.logout(request)
    return redirect('/auth/login')
