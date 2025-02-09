
---
# Proyecto Ríos del Desierto
---
---

El objetivo del presente proyecto es **consultar la información de un cliente** ingresando únicamente su número de documento y, adicionalmente, **generar un reporte en Excel** para la fidelización de los clientes que hayan superado un monto específico de compras durante el último mes.

## Contenido

- Descripción General
- Requerimientos
- Estructura del Proyecto
- Instalación y Configuración
    - Creación del Entorno Virtual
    - Instalación de Dependencias
    - Configuración de la Base de Datos
- Ejecución en Desarrollo
- Modelos y Base de Datos
- Endpoints Principales
- Frontend (Formulario de Búsqueda)
- Reporte de Fidelización
- Cómo Contribuir
- Licencia

---

## Descripción General

La aplicación ha sido desarrollada en **Python/Django** y permite llevar a cabo las siguientes acciones:

1. **Consultar** la información de un cliente por medio de una **API**, proporcionando su número de documento.
2. **Visualizar** la información obtenida en un **frontend** web de estructura sencilla.
3. **Exportar** la información del cliente en un archivo CSV u otro formato similar.
4. **Generar** un reporte en Excel que contenga a los clientes con un monto de compras superior a **5’000.000 COP** durante el último mes.

---

## Requerimientos

- Python **3.10+**
- Django
- Django REST Framework
- Pandas y openpyxl
- SQLite

---

## Estructura del Proyecto

```
p_rios/                  <-- Raíz del proyecto
├── rios_del_desierto/   <-- Proyecto Django
│   ├── manage.py
│   ├── rios_del_desierto/
│   │   ├── settings.py
│   │   ├── urls.py
│   │
│   └── clientes/        <-- Aplicación principal
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       ├── serializers.py
│       ├── templates/
│       │   └── index.html
│       ├── static/
│       │   └── js/
│       └── migrations/
└── requirements.txt
```

---

## Instalación y Configuración

### Creación del Entorno Virtual

1. Abra una terminal en la carpeta raíz del proyecto (por ejemplo, `p_rios`).
    
2. Cree el entorno virtual:
    
    ```bash
    python -m venv venv
    ```
    
3. Active el entorno virtual:
    
    - **Windows:**
        
        ```bash
        venv\Scripts\activate
        ```
        
    - **Linux/Mac:**
        
        ```bash
        source venv/bin/activate
        ```
        

### Instalación de Dependencias

Con el entorno virtual activo, instale las dependencias ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

En caso de no contar con un archivo `requirements.txt`, instale manualmente las dependencias requeridas:

```bash
pip install django djangorestframework pandas openpyxl
```

Posteriormente, guarde las dependencias ejecutando:

```bash
pip freeze > requirements.txt
```

### Configuración de la Base de Datos

El proyecto está configurado por defecto para utilizar **SQLite**. Si se requiere emplear otra base de datos (por ejemplo, PostgreSQL o MySQL), es necesario ajustar la sección `DATABASES` en el archivo `rios_del_desierto/settings.py`.

---

## Ejecución en Desarrollo

1. Ejecute las migraciones correspondientes:
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    
2. (Opcional) Cree un superusuario para acceder al panel de administración:
    
    ```bash
    python manage.py createsuperuser
    ```
    
3. Inicie el servidor de desarrollo:
    
    ```bash
    python manage.py runserver
    ```
    
4. Abra [http://127.0.0.1:8000](http://127.0.0.1:8000/) en su navegador web.
    

---

## Modelos y Base de Datos

El proyecto incluye varios modelos básicos definidos en `clientes/models.py`. Algunos de ellos son:

- **TipoDocumento:** Almacena el tipo de documento (NIT, Cédula, Pasaporte, entre otros).
- **Cliente:** Contiene la información principal del cliente, como nombre, apellido y correo electrónico.
- **Compra:** Registra cada compra realizada por un cliente, incluyendo la `fecha_compra` y el `monto` correspondiente.

---

## Endpoints Principales

1. **Búsqueda de Cliente** (GET):
    
    ```
    /api/clientes/<numero_documento>/
    ```
    
    - Retorna un JSON con la información del cliente, que incluye nombre, apellido, correo electrónico y teléfono.
2. **Reporte de Fidelización** (GET):
    
    ```
    /api/reporte_fidelizacion/
    ```
    
    - Genera y descarga un archivo en formato Excel (`.xlsx`) con los clientes que superaron **5’000.000 COP** en compras durante el último mes.

---

## Frontend (Formulario de Búsqueda)

El archivo `clientes/templates/index.html` contiene un formulario básico que permite:

- Seleccionar el tipo de documento (NIT, Cédula o Pasaporte).
- Ingresar el número de documento.
- Realizar una petición `fetch` al endpoint `/api/clientes/<numero_documento>/`.
- Mostrar la información obtenida en pantalla.
- Exportar los datos en formato CSV.

Ejemplo de uso:

1. Acceda a [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
2. Seleccione el tipo de documento (`Cédula`) e ingrese un número (`123456789`).
3. Haga clic en “Buscar”.
4. Visualice la información del cliente, en caso de que exista.
5. Haga clic en “Exportar Datos” para descargar un archivo en formato CSV.

---

## Reporte de Fidelización

Para los clientes que hayan realizado compras superiores a **5’000.000 COP** en los últimos **30 días**, el sistema genera un reporte en formato Excel. El procedimiento es el siguiente:

1. El backend, definido en `clientes/views.py`, emplea la librería **Pandas** para:
    
    - Filtrar las compras realizadas en los últimos 30 días.
    - Sumar los montos por cliente.
    - Identificar aquellos que superen el límite establecido.
    - Crear un archivo Excel y retornarlo en la respuesta HTTP.
2. Acceda a la ruta:
    
    ```
    /api/reporte_fidelizacion/
    ```
    
    El navegador descargará el archivo `reporte_fidelizacion.xlsx`.
    

---

## Cómo Contribuir

1. Realice un **fork** del repositorio.
2. Cree una rama para su funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Aplique sus cambios y realice los commits correspondientes.
4. Realice un push a su rama en el repositorio fork.
5. Cree un **Pull Request**, detallando los cambios realizados.

---

## Licencia

Este proyecto ha sido desarrollado por [metalhead13 (Alejandro A.)](https://github.com/metalhead13) exclusivamente para Falabella Colombia y el grupo Cinte.
