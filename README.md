# testdjango1
prueba con django y git

Crear el proyecto:
  1. Ubicarse en la ruta donde queremos que este
  2. django-admin startproject nombre_proyecto

Arrancar servidor:
  1. Ubicarse en la ruta del proyecto
  2. python manage.py runserver

Crear apps:
  1. Ubicarse en la ruta del proyecto
  2. python manage.py startapp nombre_app

Agregar la ruta de las plantillas:
  1. Ir a settins.py y ubicar TEMPLATES
  2. Agregar en DIR la ruta de la carpeta donde estan las plantillas

Agregar una pagina:
  1. Agreagar el documento html en la carpeta plantillas
  2. Crear la vista en views.py
  3. Importar la vista creada en urls.py y agregar el path
