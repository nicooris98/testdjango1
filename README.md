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

Cada vez que se quiere agregar una pagina primero tenemos que tener el documento html creado en la carpeta plantillas, crear la vista en views.py y agregar el path en urls.py

Hay que poner la ruta de las plantillas en settings.py en la parte de templates
