from django.shortcuts import render, HttpResponse, redirect

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
        <li>
            <a href="/contacto">Contacto</a>
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

    # Para retornar una vista se usa render
    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que esta en la vista'
    })

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir = 0):
    if redirigir == 1:
        #return redirect('/inicio/') # Forma de redirigir sin parametros
        return redirect('contacto', nombre = "Persona", apellidos = "Anonima") # Redirigir con parametros

    return render(request, 'pagina.html')

def contacto(request, nombre="", apellidos=""):
    html = ""

    if nombre and apellidos:
        html += "<p>El nombre completo es:</p>"
        html += f"<h3>{nombre} {apellidos}</h3>"
    elif nombre:
        html += "<p>El nombre es:</p>"
        html += f"<h3>{nombre}</h3>"
        
    return HttpResponse(layout + f"<h2>Contacto</h2>" + html)