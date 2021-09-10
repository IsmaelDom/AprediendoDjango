from django.shortcuts import render, HttpResponse

# Create your views here.
layout = """
    <h1>Sitio Web con Django</h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/hola-mundo">Hola Mundo</a>
        </li>
        <li>
            <a href="/pagina-pruebas">Pagina de Pruebas</a>
        </li>
    </ul>
    <hr/>
"""
def index(request):
    html = """
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
    """
    year = 2021
    while year <= 2050:

        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"

        year += 1

    html += "</ul>"

    return HttpResponse(layout + html)

def hola_mundo(request):
    return HttpResponse(layout + """
        <h1>Hola Mundo desde Django</h1>
        <h3>Bienvenido</h3>
    """)

def pagina(request):
    return HttpResponse(layout + """
        <h1>Página de la web</h1>
        <p>Crado en 2021</p>
    """)

def contacto(request, nombre, apellidos):
    return HttpResponse(layout + f"<h2>Contacto {nombre} {apellidos}</h2>")