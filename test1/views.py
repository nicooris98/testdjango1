from django.http import HttpResponse
import datetime
from django.template import Template, Context

ruta="E:/NICO/Informatica/Django/test1/test1/"

def saludo(request):#primera vista
    #documento="<html><body><h1>Primera Pagina Django</h1></body></html>"
    doc_externo=open(ruta+"plantillas/plantilla1.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
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
    