# Academia App — Gestión de Cursos

Aplicación web desarrollada con **Python y Flask** para administrar cursos académicos. Permite registrar, consultar, editar, eliminar y buscar cursos almacenados en una base de datos MySQL.

El proyecto aplica conceptos de desarrollo backend, operaciones CRUD, validación de formularios, gestión de bases de datos y protección CSRF.

## Funcionalidades

- **Registro de cursos:** creación de cursos con nombre, instructor y duración.
- **Consulta de cursos:** visualización de los cursos registrados.
- **Edición de cursos:** actualización de la información de cada curso.
- **Eliminación de cursos:** eliminación con confirmación previa.
- **Búsqueda:** filtrado por nombre del curso o instructor.
- **Validación de formularios:** comprobación de los datos ingresados.
- **Protección CSRF:** protección de formularios frente a solicitudes no autorizadas.
- **Migraciones de base de datos:** administración de cambios en el esquema mediante Flask-Migrate.

## Tecnologías utilizadas

- **Python** — lenguaje de programación.
- **Flask** — framework web.
- **Flask-SQLAlchemy** — integración con la base de datos mediante ORM.
- **MySQL** — sistema de gestión de bases de datos.
- **PyMySQL** — conector entre Python y MySQL.
- **Flask-Migrate** — migraciones del esquema de base de datos.
- **Flask-WTF** — formularios y validación.
- **python-dotenv** — gestión de variables de entorno.
- **Bootstrap 5** — diseño de la interfaz adaptable.

## Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Python 3.
- MySQL Server.
- Git.
- Un editor de código, como Visual Studio Code o PyCharm.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/DarioGM28/academia-app.git
cd academia-app
```

### 2. Crear un entorno virtual

En Windows:

```powershell
python -m venv .venv
```

Activarlo en PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Si utilizas la terminal CMD:

```cmd
.venv\Scripts\activate.bat
```

### 3. Instalar las dependencias

Con el entorno virtual activado:

```bash
python -m pip install flask flask-sqlalchemy flask-migrate pymysql python-dotenv flask-wtf
```

### 4. Configurar la base de datos

Inicia sesión en MySQL y crea la base de datos:

```sql
CREATE DATABASE academia_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

### 5. Configurar las variables de entorno

Crea un archivo `.env` en la raíz del proyecto con la siguiente estructura:

```dotenv
SECRET_KEY=pon_aqui_una_clave_secreta
DB_HOST=localhost
DB_PORT=3306
DB_USER=tu_usuario
DB_PASSWORD=tu_contrasena
DB_NAME=academia_db
```

Reemplaza los valores de ejemplo por los datos de tu instalación local de MySQL. La clave secreta debe ser única y privada.

**Importante:** no publiques el archivo `.env` ni compartas tus contraseñas. El repositorio debe incluir un `.gitignore` que excluya `.env` y `.venv/`.

### 6. Inicializar las migraciones

Si el proyecto ya incluye la carpeta `migrations/`, continúa con el paso siguiente. Si no existe y la aplicación ya está configurada para Flask-Migrate, ejecuta:

```bash
flask --app app db init
flask --app app db migrate -m "Creacion inicial de tablas"
flask --app app db upgrade
```

Si el repositorio ya contiene migraciones, no vuelvas a ejecutar `db init`; aplica las migraciones existentes con `flask --app app db upgrade`.

### 7. Ejecutar la aplicación

Con el entorno virtual activado:

```bash
python app.py
```

Abre en tu navegador la dirección local que indique la terminal, normalmente:

```text
http://127.0.0.1:5000
```

## Estructura del proyecto

```text
academia-app-flask/
├── app.py
├── extensions.py
├── models.py
├── forms.py
├── services/
│   └── curso_service.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── agregar_curso.html
│   └── editar_curso.html
├── migrations/
├── .env
├── .gitignore
└── README.md
```

La estructura puede variar según los archivos incluidos en el repositorio. El archivo `.env` se utiliza localmente y no debe subirse a Git.

## Conceptos aplicados

- Desarrollo de aplicaciones web con Flask.
- Separación de responsabilidades entre rutas, modelos, formularios y servicios.
- Operaciones CRUD sobre una base de datos relacional.
- Consultas y filtros mediante SQLAlchemy.
- Validación de datos del usuario.
- Protección CSRF en formularios.
- Uso de variables de entorno para la configuración.
- Control de versiones con Git.

## Autor

**Dario Gómez**

Ingeniero Electrónico | Desarrollo de Software

- GitHub: [DarioGM28](https://github.com/DarioGM28)

---

*Proyecto de aprendizaje enfocado en el desarrollo backend con Python, Flask y MySQL.*
