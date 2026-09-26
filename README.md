Proyecto Django minimalista para un menú de restaurante.

Instrucciones rápidas (Windows PowerShell):

1. Crear entorno virtual e instalar dependencias:

```powershell
python -m venv .venv
.venv\Scripts\Activate
pip install -r requirements.txt
```

2. Aplicar migraciones y crear superusuario:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

3. Ejecutar el servidor:

```powershell
python manage.py runserver
```

`runserver` es sólo para desarrollo. En el servidor, configura estas variables de entorno antes de iniciar Django:

- `DJANGO_SECRET_KEY`: clave secreta larga y única para esa instalación.
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS`: nombres de dominio permitidos, separados por comas.

El servidor debe ejecutar `python manage.py migrate` y `python manage.py createsuperuser`. La base `db.sqlite3` local no se incluye en el repositorio.

4. Importar platillos desde CSV (opcional):

Prepara un CSV con encabezados: `name,description,price,image_filename,available`
Ejemplo (file `dishes.csv`):

```csv
name,description,price,image_filename,available
Tacos al Pastor,Deliciosos tacos con piña,45.00,tacos.jpg,True
Ensalada Cesar,Lechuga, queso y aderezo,38.50,ensalada.jpg,True
```

Coloca las imágenes en `media/dishes/` o en otra carpeta y usa la opción `--media-dir`.

Comando de importación:

```powershell
python manage.py import_dishes path\to\dishes.csv --media-dir path\to\media\dishes
```

5. Administración y edición:

- Sólo el administrador puede crear o editar platillos desde el panel de Django Admin (`/admin/`).
- La interfaz pública muestra el menú pero no permite agregar ni editar platillos.
- Para quitar un platillo temporalmente, selecciónalo en la lista del admin y usa `Ocultar platillos del menú público`. Esto conserva toda su información.
- Para volver a publicarlo, selecciónalo y usa `Mostrar platillos en el menú público`.

Notas:
- Las imágenes subidas se guardan en `media/dishes/`.
- Si necesitas que vuelva a permitir la creación pública (por ejemplo, mediante autenticación), dímelo y lo habilito.
- La base de datos local no se publica; crea el usuario administrador directamente en el servidor.
