# Cineon — API REST para un sistema de cine

## Descripción del proyecto

Cineon es un proyecto académico desarrollado con Django y Django REST Framework para administrar la información de un sistema de cine. El proyecto incluye una API REST que permite consultar y registrar información mediante endpoints y solicitudes HTTP.

El sistema contempla la administración de usuarios, películas, salas, asientos, funciones, reservas, pagos y detalles de las reservas. También cuenta con una interfaz web desarrollada con HTML, CSS y JavaScript.

## Objetivo

Desarrollar una API REST que permita gestionar la información principal de un sistema de cine, utilizando modelos de Django, serializadores, vistas y rutas para organizar el acceso a los datos.

## Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Django:** framework para el desarrollo backend.
- **Django REST Framework:** herramientas para crear la API REST.
- **PostgreSQL:** sistema de gestión de bases de datos.
- **HTML:** estructura de la interfaz web.
- **CSS:** estilos visuales de la página.
- **JavaScript:** funcionalidades de la interfaz.
- **Git y GitHub:** control de versiones y alojamiento del código fuente.

## Modelos del sistema

El proyecto contiene ocho modelos principales:

| Modelo | Descripción |
|---|---|
| Usuario | Almacena la información de los usuarios del sistema. |
| Pelicula | Contiene la información de las películas disponibles. |
| Sala | Representa las salas de cine. |
| Asiento | Registra los asientos pertenecientes a las salas. |
| Funcion | Contiene información de las funciones, películas, horarios y salas. |
| Reserva | Registra las reservas realizadas por los usuarios. |
| Pago | Almacena información relacionada con los pagos de las reservas. |
| DetalleReserva | Relaciona las reservas con los asientos correspondientes. |

## Endpoints de la API

La API utiliza las siguientes rutas para acceder a sus recursos:

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

### Métodos HTTP

- **GET:** consulta registros.
- **POST:** registra nuevos datos.
- **PUT:** actualiza un registro completo.
- **PATCH:** actualiza parcialmente un registro.
- **DELETE:** elimina un registro.

Los endpoints individuales utilizan el identificador del registro. Por ejemplo:

`/api/peliculas/1/`

La disponibilidad de los métodos depende de la configuración de las vistas y las rutas de Django REST Framework.

## Requisitos previos

Para ejecutar el proyecto se necesita:

- Python instalado.
- pip.
- PostgreSQL instalado y funcionando.
- Git instalado.
- Un editor de código, como Visual Studio Code.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/bjarillo29/Cineon-API-Django.git
cd Cineon-API-Django
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

En Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Si utilizas el símbolo del sistema de Windows (CMD):

```bat
venv\Scripts\activate.bat
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 5. Configurar la base de datos

Crea una base de datos en PostgreSQL y configura la conexión en los ajustes del proyecto o mediante las variables de entorno utilizadas por la aplicación.

No publiques contraseñas, claves ni otros datos privados en el repositorio.

### 6. Aplicar las migraciones

```bash
python manage.py migrate
```

### 7. Iniciar el servidor

```bash
python manage.py runserver
```

Abre las siguientes direcciones en el navegador:

- **Página principal:** http://127.0.0.1:8000/
- **Administración de Django:** http://127.0.0.1:8000/admin/
- **Raíz de la API:** http://127.0.0.1:8000/api/

El servidor de desarrollo está destinado a pruebas locales.

## Pruebas realizadas

Se utilizaron las vistas navegables de Django REST Framework para probar los endpoints de los ocho modelos.

Las pruebas incluyeron:

- Consultas mediante GET.
- Registro de datos mediante POST.
- Verificación de las respuestas HTTP.
- Comprobación de relaciones entre registros mediante sus identificadores.

Las pruebas de GET y POST se realizaron para Usuarios, Películas, Salas, Asientos, Funciones, Reservas, Pagos y DetalleReserva.

## Estructura del proyecto

La estructura principal del proyecto es la siguiente:

```text
core_cine_bryan/
├── cine/
│   ├── migrations/
│   ├── static/
│   │   └── cine/
│   │       ├── css/
│   │       │   └── estilos.css
│   │       └── js/
│   │           └── script.js
│   ├── Templates/
│   │   └── Cine/
│   │       ├── Inicio.html
│   │       └── detalle_pelicula.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── core_cine_bryan/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── .gitignore
├── docker-compose.yml
├── manage.py
├── readme.md
└── requirements.txt
```

## Autor y repositorio

**Proyecto:** Cineon — API REST para un sistema de cine.

**Repositorio de GitHub:** [https://github.com/bjarillo29/Cineon-API-Django](https://github.com/bjarillo29/Cineon-API-Django)

## Consideraciones de seguridad

Este proyecto fue desarrollado con fines académicos. Antes de utilizarlo en un entorno de producción sería necesario revisar la autenticación, los permisos, la validación de los datos, el tratamiento seguro de contraseñas y la configuración del servidor.

El archivo `.env` y cualquier archivo que contenga credenciales deben mantenerse fuera del repositorio público.

## Conclusión

El desarrollo de Cineon permitió practicar la creación de modelos, serializadores, vistas y rutas mediante Django REST Framework. También permitió comprobar la comunicación con la API a través de solicitudes HTTP y comprender cómo se relacionan los datos de un sistema de cine.
