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
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'  # Placeholder
            id_persona = input('Digite un numero para el id_persona: ')
            cursor.execute(sentencia, (id_persona, ))  # De esta manera ejecutamos la sentencia
            registros = cursor.fetchone()  # Recuperamos todos los registros que seran una lista

            # Imprimimos todos los datos que se encuentran en la BD
            print(registros)

except Exception as error:
    print(f'Ocurrio un Error: {error}')
finally:
    conexion.close()
