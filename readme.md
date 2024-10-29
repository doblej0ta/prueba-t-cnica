# Stations API

## Descripción

Este proyecto es una API RESTful para gestionar estaciones con información geográfica, incluyendo la creación, listados y búsqueda de estaciones cercanas utilizando Django y PostgreSQL con la extensión PostGIS.

## Tecnologías utilizadas

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL
- PostGIS
- GDAL

## Requisitos previos

1. Python 3.x instalado
2. PostgreSQL con la extensión PostGIS
3. GDAL instalado y correctamente configurado

## Instalación

1. Clona este repositorio:
   bash
   git clone [<repositorio-url>](https://github.com/doblej0ta/prueba-t-cnica)
   cd prueba-t-cnica
   

2. Crea un entorno virtual e instálalo:
   bash
   python -m venv env
   source env/bin/activate  # En Windows usa env\Scripts\activate
   pip install -r requirements.txt
   

3. Configura la base de datos en `settings.py`:
   python
   DATABASES = {
       'default': {
           'ENGINE': 'django.contrib.gis.db.backends.postgis',
           'NAME': 'nombre_base_de_datos',
           'USER': 'root',
           'PASSWORD': 'qwerty123',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   

4. Realiza las migraciones:
   bash
   python manage.py migrate
   

5. Crea un superusuario:
   bash
   python manage.py createsuperuser
   

6. Ejecuta el servidor:
   bash
   python manage.py runserver
   

## Endpoints

### Crear una estación

- **URL:** `/api/stations/`
- **Método:** `POST`
- **Cuerpo (JSON):**
  json
  {
      "name": "Estación 1",
      "latitude": 10.123456,
      "longitude": -74.123456
  }
  

### Listar estaciones

- **URL:** `/api/stations/`
- **Método:** `GET`
- **Respuesta:**
  json
  [
      {
          "id": 1,
          "name": "Estación 1",
          "latitude": 10.123456,
          "longitude": -74.123456
      }
  ]
  

### Estación más cercana

- **URL:** `/api/stations/{id}/nearby/`
- **Método:** `GET`
- **Descripción:** Devuelve la estación más cercana a la estación con el ID especificado.

## Pruebas

Puedes utilizar Postman o cualquier cliente HTTP para probar los endpoints. Asegúrate de enviar las solicitudes a `http://localhost:8000/api/stations/`.

### Ejemplo de prueba en Postman

1. **Crear una estación:**
   - Método: `POST`
   - URL: `http://localhost:8000/api/stations/`
   - Cuerpo: (JSON)
   json
   {
       "name": "Estación 1",
       "latitude": 10.123456,
       "longitude": -74.123456
   }
   

2. **Listar estaciones:**
   - Método: `GET`
   - URL: `http://localhost:8000/api/stations/`

3. **Obtener estación más cercana:**
   - Método: `GET`
   - URL: `http://localhost:8000/api/stations/{id}/nearby/`

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`)
3. Realiza tus cambios y haz un commit (`git commit -m 'Agregada nueva característica'`)
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.