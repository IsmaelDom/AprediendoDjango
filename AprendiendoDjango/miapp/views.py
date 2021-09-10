from django.shortcuts import render, HttpResponse

# Create your views here.
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

    return HttpResponse(html)

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