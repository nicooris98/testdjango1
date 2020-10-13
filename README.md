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
  3. El comando anterior crea una carpeta con el nombre que pusimos
  4. Ir a la carpeta de la app y luego a models.py
  5. Crear las clases que seran las tablas de la base de datos
  6. Agregar la app en settings.py en la parte de INSTALLED_APPS
  7. (Opcional) Para chequear que todo este bien python manage.py check nombre_app y si esta todo bien deberia salir System check identified no issues (0 silenced)

Crear la base de datos(sqlite3):
  1. Ubicarse en la ruta del proyecto
  2. python manage.py makemigrations

Agregar la ruta de las plantillas:
  1. Ir a settins.py y ubicar TEMPLATES
  2. Agregar en DIR la ruta de la carpeta donde estan las plantillas

Agregar una pagina:
  1. Agreagar el documento html en la carpeta plantillas
  2. Crear la vista en views.py
  3. Importar la vista creada en urls.py y agregar el path
