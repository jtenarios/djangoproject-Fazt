admin:
    * jtena
    * 1234
    * jtena@test.test

https://www.youtube.com/watch?v=T1intZyhXDU&ab_channel=Fazt

Instrucciones:

instalar virtualizador:
    D:\Desarrollo\djangoproject>pip install virtualenv
crear carpeta del projecto
    D:\Desarrollo\djangoproject>virtualenv venv
activar el entorno virtual
    D:\Desarrollo\djangoproject>.\venv\Scripts\activate

Instalar djando
    D:\Desarrollo\djangoproject>pip install django
Ver si djando está instalado
    D:\Desarrollo\djangoproject>django-admin --version

Crear projecto
    "D:\Desarrollo\djangoproject>django-admin startproject mysite  ."- mysite es el nombre del projecto - el punto es para que no cree una nueva carpeta, sino que use el la ruta actual
    https://youtu.be/T1intZyhXDU?t=1293

Ejecutar proyecto
    D:\Desarrollo\djangoproject>python manage.py runserver
Cambiar puerto del projecto
    D:\Desarrollo\djangoproject>python manage.py runserver 3000

Crear nueva aplicación dentro del projecto - https://youtu.be/T1intZyhXDU?t=2106
    python manage.py startapp myapp

Crear ruta de directorios URLS
    https://youtu.be/T1intZyhXDU?t=3018

Migrar/crear base de datos
    App Visualizar BD: https://sqlitebrowser.org/
    D:\Desarrollo\djangoproject>python manage.py makemigrations
    D:\Desarrollo\djangoproject>python manage.py migrate

Crear tablas en la BD
    https://youtu.be/T1intZyhXDU?t=3573

Conectar la BD al proyecto
    https://youtu.be/T1intZyhXDU?t=3596

Interactuar con la BD
    https://youtu.be/T1intZyhXDU?t=4162
Insert
    >>> from myapp.models import Project, Task 
    >>> p=Project(name="aplicacion movil")
    >>> p.save()
Select
    >>> Project.objects.all() -- Mostrar tod0s
    >>> Project.objects.get(id=1) -- Mostrar solo id=1
filtros
    >>> Project.objects.filter(name__startswith="aplicacion") 
    https://youtu.be/T1intZyhXDU?t=4748

Recibir parámetros de la URL
    https://youtu.be/T1intZyhXDU?t=4877

Pasar parámetros de backend al template HTML
    https://youtu.be/T1intZyhXDU

Recorres datos de una lista de elementos
    https://youtu.be/T1intZyhXDU?t=7295

If condicional
    https://youtu.be/T1intZyhXDU?t=8232

Resto de instrucciones
    https://jinja.palletsprojects.com/en/3.1.x/

Plantillas o componentes que se pueden usar en diferentes partes
    https://youtu.be/T1intZyhXDU?t=8535

Crear formularios desde python
    https://youtu.be/T1intZyhXDU?t=9099

Asignar nombres a las URLs
    https://youtu.be/T1intZyhXDU?t=10604

Plantilla error 404 page not found
    https://youtu.be/T1intZyhXDU?t=11929

Aplicar estilos desde python
    https://youtu.be/T1intZyhXDU?t=12417

Configurar subida a produccion
    https://youtu.be/e6PkGDH4wWA?t=10335

Conectar a BD PostgreSQl
    https://youtu.be/e6PkGDH4wWA?t=10567