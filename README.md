# Clase #2

El objetivo de laclase conocer el uso de diagramas UML con el uso de los ORM en Python.

Diagrama UML de venterianaria.

![UML](img/Diagrama_UML_CLASE%20%232.png)

## Requeriemientos

- SLQAlchemy
- PyMySQL
- Base datos realacional (Mariadb, Mysql, Postgres)


## Ejecutar proyecto con base datos SQLITE

Solamente se corre *main.py* en cuál carga información inicial.

## Ejecutar  proyecto con base datos robusta

Se deberá argregar los archivos de configuración de la conexion

```database.connector.py
   engine = create_engine('mysql+pymysql://root:clase2@localhost/taller')
```