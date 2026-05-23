from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def usuarios(request):
    lista_user = [
        {"nome": "Paula", "matricula": 20, "idade": 17, "cidade": "BS"},
        {"nome": "Anna Vitória", "matricula": 8, "idade": 17, "cidade": "BS"},
        {"nome": "Camily", "matricula": 34, "idade": 64, "cidade": "BS"},
        {"nome": "Lula", "matricula": 13, "idade": 18, "cidade": "Presidencia"},
        {"nome": "Bolsonaro", "matricula": 22, "idade": 19, "cidade": "Prisão"},
    ]

    context = {
        "usuarios": lista_user,
    }
  
    return render(request, "usuarios.html", context)