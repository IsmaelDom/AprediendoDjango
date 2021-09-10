from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("""
        <h1>Inicio</h1>
    """)

def hola_mundo(request):
    return HttpResponse("""
        <h1>Hola Mundo desde Django</h1>
        <h3>Bienvenido</h3>
    """)

def pagina(request):
    return HttpResponse("""
        <h1>Página de la web</h1>
        <p>Crado en 2021</p>
    """)