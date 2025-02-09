Proyecto Ríos del Desierto

Objetivo **consultar la información de un cliente** ingresando únicamente su número de documento y, además, **generar un reporte en Excel** para la fidelización de los clientes que hayan superado un monto específico de compras en el último mes.

## Contenido

- [Descripción General](https://chatgpt.com/c/67a81106-96d4-8003-b163-1e9d0042be2a#descripci%C3%B3n-general)
- [Requerimientos](https://chatgpt.com/c/67a81106-96d4-8003-b163-1e9d0042be2a#requerimientos)
- [Estructura del Proyecto](https://chatgpt.com/c/67a81106-96d4-8003-b163-1e9d0042be2a#estructura-del-proyecto)
- [Instalación y Configuración](https://chatgpt.com/c/67a81106-96d4-8003-b163-1e9d0042be2a#instalaci%C3%B3n-y-configuraci%C3%B3n)
    - [Creación del Entorno Virtual](https://chatgpt.com/c/67a81106-96d4-8003-b163-1e9d0042be2a#creaci%C3%B3n-del-entorno-virtual)
    - [Instalación de Dependencias](https://chatgpt.com/c/67a81106-96d4-8003-b163-1e9d0042be2a#instalaci%C3%B3n-de-dependencias)
    - [Configuración de la Base de Datos](https://chatgpt.com/c/67a81106-96d4-8003-b163-1e9d0042be2a#configuraci%C3%B3n-de-la-base-de-datos)
- [Ejecución en Desarrollo](https://chatgpt.com/c/67a81106-96d4-8003-b163-1e9d0042be2a#ejecuci%C3%B3n-en-desarrollo)
- [Modelos y Base de Datos](https://chatgpt.com/c/67a81106-96d4-8003-b163-1e9d0042be2a#modelos-y-base-de-datos)
- [Endpoints Principales](https://chatgpt.com/c/67a81106-96d4-8003-b163-1e9d0042be2a#endpoints-principales)
- [Frontend (Formulario de Búsqueda)](https://chatgpt.com/c/67a81106-96d4-8003-b163-1e9d0042be2a#frontend-formulario-de-b%C3%BAsqueda)
- [Reporte de Fidelización](https://chatgpt.com/c/67a81106-96d4-8003-b163-1e9d0042be2a#reporte-de-fidelizaci%C3%B3n)
- [Cómo Contribuir](https://chatgpt.com/c/67a81106-96d4-8003-b163-1e9d0042be2a#c%C3%B3mo-contribuir)
- [Licencia](https://chatgpt.com/c/67a81106-96d4-8003-b163-1e9d0042be2a#licencia)

---

## Descripción General

La aplicación ha sido desarrollada en **Python/Django** y permite llevar a cabo las siguientes acciones:

1. **Buscar** información de un cliente (por número de documento) mediante una **API**.
2. **Mostrar** esa información en un **frontend** web sencillo.
3. **Exportar** la información del cliente en un archivo CSV (o formato similar).
4. **Generar** un reporte en Excel que muestre a los clientes con un monto de compras mayor a 5’000.000 COP en el último mes.

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
p_rios/                  <-- Raíz 
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

1. Abra una terminal en la carpeta raíz del proyecto (`p_rios`).
    
2. Cree el entorno virtual:
    
    ```bash
    python -m venv venv
    ```
    
3. Active el entorno virtual:
    
    - Windows:
        
        ```bash
        venv\Scripts\activate
        ```
        
    - Linux/Mac:
        
        ```bash
        source venv/bin/activate
        ```
        

### Instalación de Dependencias

Con el entorno virtual activo, instalre las dependencias ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```


### Configuración de la Base de Datos

El proyecto está configurado para utilizar **SQLite** por defecto (en `settings.py`).  
Si se requiere emplear otra base de datos (por ejemplo, PostgreSQL o MySQL), ajuste la sección `DATABASES` en `rios_del_desierto/settings.py`.

---

## Ejecución en Desarrollo

1. Ejecute las migraciones:
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    
2. Ejecute el servidor de desarrollo:
    
    ```bash
    python manage.py runserver
    ```
    
4. Abra [http://127.0.0.1:8000](http://127.0.0.1:8000/) en su navegador.

---

## Modelos y Base de Datos

El proyecto incluye varios modelos básicos definidos en `clientes/models.py`. Algunos de ellos son:

- **TipoDocumento**: para almacenar el tipo de document.
- **Cliente**: almacena la información principal del cliente .
- **Compra**: registra cada compra hecha por un cliente, incluyendo `fecha_compra` y `monto`.

---

## Endpoints Principales

1. **Búsqueda de Cliente** (GET):
    
    ```
    /api/clientes/<numero_documento>/
    ```
    

2. **Reporte de Fidelización** (GET):
    
    ```
    /api/reporte_fidelizacion/
    ```
    
    - Genera y descarga un archivo Excel `.xlsx` con los clientes que superaron **5.000.000** de COP en el último mes.

---

## Frontend

El archivo `clientes/templates/index.html` contiene un **formulario** minimalista que permite:

- Selecciona el **tipo de documento** (NIT, Cédula o Pasaporte).
- Ingresa el **número de documento**.
- Al enviar, se realiza una **petición fetch** al endpoint `/api/clientes/<numero_documento>/`.
- Muestra la información en pantalla 
- Permite **exportar** los datos en formato CSV.

Ejemplo de uso:

1. Acceder a [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
2. Seleccionar `Cedula` y escribir `123456789`.
3. Hacer clic en “Buscar”.
4. Ver la información del cliente (si existe).
5. Hacer clic en “Exportar Datos” para descargar un `.csv`.

---

## Reporte de Fidelización

Para los clientes que hayan realizado compras superiores a **5’000.000 COP** en los últimos **30 días**, el sistema genera un reporte en formato Excel. El procedimiento es el siguiente:

1. El backend en `clientes/views.py` utiliza **Pandas** para:
    
    - Filtrar las compras de los últimos 30 días.
    - Sumar los montos por cliente.
    - Filtrar quienes superen 5’000.000.
    - Crear un archivo Excel y retornarlo en la respuesta HTTP.
2. Acceda a la ruta:
    
    ```
    /api/reporte_fidelizacion/
    ```
    
    El navegador descargará el archivo `reporte_fidelizacion.xlsx`.
    



---

## Licencia

Este proyecto ha sido desarrollado por  [metalhead13 (Alejandro A.)](https://github.com/metalhead13)  exclusivamente para Falabella Colombia y el grupo Cinte. 
