import psycopg2  # Esto es para conectarnos a Postgres

# Creamos la connexion con postgres
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try:
    with conexion:
        with conexion.cursor() as cursor:

            cursor = conexion.cursor()
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'  # Placeholder
            entrada = input('Digite los id_persona a buscar (separados por coma): ')
            llaves_primarias = (tuple(entrada.split(', ')), )
            cursor.execute(sentencia, llaves_primarias)  # De esta manera ejecutamos la sentencia
            registros = cursor.fetchall()  # Recuperamos todos los registros que seran una lista
            for registro in registros:
                # Imprimimos todos los datos que se encuentran en la BD
                print(registro)

except Exception as error:
    print(f'Ocurrio un Error: {error}')
finally:
    conexion.close()