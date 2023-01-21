## Correr la aplicacion

Para correr la aplicación de flask ejecutamos

```
flask --debug run
```

## Para ejecutar las migraciones

```
flask db init
flask db migrate -m "primera migracion"
flask db upgrade
```

## Para correr el frontend

```
npm install
npm run dev
```