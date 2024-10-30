# Usa una imagen base de Python
FROM python:3.12

# Instala las dependencias del sistema necesarias
RUN apt-get update && \
    apt-get install -y \
    gdal-bin \
    libgdal-dev \
    && apt-get clean

# Establece la variable de entorno para GDAL
ENV GDAL_VERSION=3.5.1

# Establece la variable de entorno para la biblioteca de GDAL
ENV GDAL_LIBRARY_PATH=/usr/lib/libgdal.so

WORKDIR /app

# Instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY . .

# Expone el puerto que utilizará tu aplicación
EXPOSE 8000

# Configura la base de datos en espera
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]