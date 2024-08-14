# API REST para Music Player

Este proyecto es el backend para un reproductor de MP3 llamado **Music Player**. La API está construida con **FastAPI** y utiliza una base de datos relacional **MySQL**.

## Endpoints de la API

### Búsqueda de Música

- **GET** `/search`
  - **Descripción**: Permite buscar por artista, álbum o nombre de la canción.
  - **Params**:
    - `search_data`: Nombre del artista.
    - `search_data`: Nombre del álbum.
    - `search_data`: Nombre de la canción.

### Autenticación y Autorización

- **POST** `/login`
  - **Descripción**: Permite realizar el login y obtener un token JWT.
  - **Body**: **form-data***
    - `username`: Nombre de usuario.
    - `password`: Contraseña.

- **GET** `/login/me`
  - **Descripción**: Prueba la autorización mostrando la información del usuario autenticado.
  - **Authorization**:
    - `Type`: Bearer Token.
    - `Token`: Token generado en el login.

### Gestión de Usuarios

- **POST** `/users/`
  - **Descripción**: Crea un nuevo usuario.
  - **Body**:**JSON**
    - `username`: Nombre para hacer login.
    - `full_name`: Nombre y apellidos del usuario.
    - `email`: Correo electrónico.
    - `role`: Rol del ususario (tipo: admin o user).
    - `type_license`: Tipo de licencia (free o premium).
    - `disabled`: Estado del la cuenta del usuario (true o false).
    - `password`: Contraseña.


- **PUT** `/users/{id_user}`
  - **Descripción**: Actualiza un usuario existente.
  - **Body**:**JSON**
    - `username`: Nombre para hacer login.
    - `full_name`: Nombre y apellidos del usuario.
    - `email`: Correo electrónico.
    - `role`: Rol del ususario (tipo: admin o user).
    - `type_license`: Tipo de licencia (free o premium).
    - `disabled`: Estado del la cuenta del usuario (true o false).
    - `password`: Contraseña.

- **GET** `/users`
  - **Descripción**: Obtiene todos los usuarios registrados en la base de datos.

- **GET** `/users/{id_user}`
  - **Descripción**: Obtiene un usuario por ID.
  
- **DELETE** `/users/{id_user}`
  - **Descripción**: Elimina un usuario por su ID.

### Extracción de Metadatos

- **GET** `/extract`
  - **Descripción**: Extrae los metadatos de archivos MP3 contenidos en un directorio y los pasa a la base de datos.
  - **Params**:
    - `directory_path`: Ruta del directorio que contiene los archivos MP3.

## Instalación de Dependencias

Para instalar las librerías necesarias para este proyecto, usa los siguientes comandos:

| Librería                | Comando de Instalación                            |
|-------------------------|---------------------------------------------------|
| **FastAPI, Uvicorn y**  | `pip install fastapi uvicorn sqlalchemy pymysql`  |
| **MySQL Connector**     |                                                   |
| **jose (JWT)**          | `pip install python-jose[cryptography]`           |
| **Pydantic**            | `pip install pydantic` (incluido con FastAPI)     |
| **Typing**              | `pip install typing` (incluido con Python 3.5+)   |
| **Mutagen**             | `pip install mutagen`                             |

## Configuración de la Base de Datos

Asegúrate de tener una base de datos MySQL configurada y accesible. Actualiza los parámetros de conexión en el archivo de configuración de tu aplicación FastAPI.

## Ejecución del Servidor

Para iniciar el servidor, usa el siguiente comando:

```bash
uvicorn app.main:app --reload
