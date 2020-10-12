from django.http import HttpResponse
import datetime
from django.template import Template, Context

ruta="E:/NICO/Informatica/Django/test1/test1/"

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):#primera vista
    #documento="<html><body><h1>Primera Pagina Django</h1></body></html>"
    #nombre="Ysidoro"
    #apellido="Oris"
    p1=Persona("Nicolas Ysidoro", "Oris")
    ahora=datetime.datetime.now()
    doc_externo=open(ruta+"plantillas/plantilla1.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora})
    documento=plt.render(ctx)
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Adios")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""
    <html>
    <body>
    <h2>
    Fecha y Hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)

def calculaEdad(request, edad, ano):
    #edadActual=22
    periodo=ano-2020
    edadFutura=edad+periodo
    documento="""<html>
    <body>
    <h2>
    En el año %s tendras %s años
    </h2>
    </body>
    </html>""" %(ano, edadFutura)
    return HttpResponse(documento)
    