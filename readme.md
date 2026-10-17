# Cineon — API REST para un sistema de cine

## Descripción

Cineon es un proyecto académico desarrollado con Django y Django REST Framework. Su objetivo es proporcionar una API REST para administrar la información de un sistema de cine mediante endpoints que permiten consultar y registrar datos.

El proyecto incluye ocho modelos principales: Usuario, Pelicula, Sala, Asiento, Funcion, Reserva, Pago y DetalleReserva.

## Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- PostgreSQL
- HTML, CSS y JavaScript para la interfaz web del proyecto

## Requisitos

- Python 3 instalado.
- pip.
- PostgreSQL instalado y en ejecución.
- Git, para clonar y administrar el repositorio.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone URL_DE_TU_REPOSITORIO
   cd NOMBRE_DE_LA_CARPETA
   ```

2. Crea y activa un entorno virtual:

   En Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

   Este comando requiere que el archivo `requirements.txt` esté incluido en el repositorio.

4. Configura las variables de entorno o los datos de conexión de PostgreSQL según la configuración del proyecto. No publiques contraseñas reales ni otros secretos.

5. Aplica las migraciones:

   ```bash
   python manage.py migrate
   ```

6. Inicia el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

7. Abre en el navegador:

   `http://127.0.0.1:8000/`

## Endpoints disponibles

| Recurso | Endpoint |
|---|---|
| Usuarios | `/api/usuarios/` |
| Películas | `/api/peliculas/` |
| Salas | `/api/salas/` |
| Asientos | `/api/asientos/` |
| Funciones | `/api/funciones/` |
| Reservas | `/api/reservas/` |
| Pagos | `/api/pagos/` |
| Detalles de reserva | `/api/detalles-reserva/` |

Los endpoints de colección permiten consultar registros con GET y crear registros con POST. Los endpoints individuales utilizan un identificador y permiten consultar, actualizar o eliminar un registro mediante los métodos HTTP que admite la configuración de la API.

## Ejemplos de uso

Consultar las películas:

```http
GET http://127.0.0.1:8000/api/peliculas/
```

Consultar los usuarios:

```http
GET http://127.0.0.1:8000/api/usuarios/
```

Registrar información: abre el endpoint correspondiente y utiliza el formulario POST de Django REST Framework, enviando los campos requeridos por el modelo.

## Pruebas

Se realizaron pruebas de solicitudes GET y POST para los ocho modelos utilizando la interfaz navegable de Django REST Framework.

## Autor

Proyecto académico Cineon.

## Nota

Este proyecto se desarrolló con fines educativos. Para utilizarlo en producción sería necesario reforzar aspectos como la autenticación, la autorización, la protección de datos y la configuración segura del servidor.