# Para Replicar la página
## Clonar el repo
```
git clone https://github.com/Just-a-Spider/Estructura-De-Datos-Class-Page.git
cd Estrucutra-De-Datos-Page
```

## Crear el entorno virtual
```
python -m venv venv
./venv/Scripts/activate
```

## Hacer las migraciones y cargar algunos ejercicios
```
python backend/manage.py makemigrations
python backend/manage.py migrate
python backend/manage.py loaddata whole.json
```

## Lanzar en local
```
python backend/manage.py runserver
```

>[!IMPORTANT]
>Para agregar más problemas crear un superuser
>```
>python backend/manage.py createsuperuser
>```
>Y manejarlo desde la página de admin
