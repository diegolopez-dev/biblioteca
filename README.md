<h1 align="center">📚 API de Biblioteca con FastAPI, MySQL y Jinja2 📖</h1>

<p align="center">
    <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI Logo" width="200">
</p>

## Descripción

Este proyecto es una API construida con FastAPI que utiliza una base de datos MySQL para gestionar una biblioteca de libros. La aplicación también hace uso de Jinja2 como motor de plantillas para la interfaz de usuario, permitiendo a los usuarios ver, crear,actualizar y borrar libros.

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias requeridas utilizando el comando `pip install -r requirements.txt`.

## Configuración

Antes de ejecutar la API, asegúrate de configurar la conexión a la base de datos MySQL en el archivo de configuración. Se recomienda utilizar variables de entorno para almacenar la información de la base de datos de forma segura.

## Uso

Una vez instaladas las dependencias y configurada la conexión a la base de datos, puedes iniciar la API ejecutando el archivo `uvicorn main:app --reload`. 
La aplicación estará disponible en `http://localhost:8000`.

### Endpoints Principales

- ✔️ `GET /books`: Obtiene la lista de todos los libros en la biblioteca.
- ✔️ `POST /books`: Permite crear un nuevo libro en la biblioteca.
- ✔️ `PUT /books/:id`: Permite actualizar la información de un libro existente.
- ✔️ `DELETE /books/:id`: Permite eliminar un libro de la biblioteca.

## Interfaz de Usuario

La aplicación incluye una interfaz de usuario construida con Jinja2 que facilita a los usuarios interactuar de forma visual con la biblioteca de libros.
