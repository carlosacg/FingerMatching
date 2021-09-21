# Proyecto Final Metodos Numericos

## Como ejecutar el programa.
Windows:

1. Descargamos e instalamos Python 3.4 para Windows
https://www.python.org/downloads/

2. Agregaremos Python a las variables de entorno de nuestro sistema si es que no se agregaron durante la instalación para que así podamos ejecutarlo desde la terminar/cmd.
Las cuales serían: C:\Python34 y C:\Python34\Scripts

3. Ejecutamos Pip para verificar que esté instalado correctamente y también la versión
```
pip --version
```
4. Instalamos Virtualenv con
```
pip install virtualenv
```

5. Verificamos la versión de Virtualenv

```
virtualenv --version
```

6. Crearemos un entorno virtual con Python

```
virtualenv test
```

7. Iniciamos el entorno virtual
```
.\test\Scripts\activate
```

8. Instalamos los requerimientos del archivo requirements.txt
```
pip install requierements.txt
```

9. Ejecutamos el servidor de Django
```
python manage.py runserver 8080
```

10. En nuestro navegador de preferencia escribiremos en url
```
localhost:8080
```