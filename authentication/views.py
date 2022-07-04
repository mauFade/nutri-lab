from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    """"Função para fazer cadastro de um novo usuário"""
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        name = request.POST.get("usuario")
        email = request.POST.get("email")
        password = request.POST.get("senha")
        confirm_password = request.POST.get("confirmar_senha")

        if password != confirm_password:
            return HttpResponse("Senhas inválidas")
        elif password == confirm_password:
            return HttpResponse(f"{name}, {email}, {password}, {confirm_password}")

def login(request):
    """"Função para fazer login"""
    return HttpResponse("Página de login")
