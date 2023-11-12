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

            sentencia = 'DELETE FROM persona WHERE id_persona = %s'
            entrada = input('Digite el numero de registro a eliminar: ')
            valores = (entrada,)  # Es una Tupla de valores
            cursor.execute(sentencia, valores)  # executemany agrega los nuevos registros y los guarda

            registros_eliminados = cursor.rowcount  # Esto es para igresar columnas
            print(f'Los registros eliminados fueron : {registros_eliminados}')

except Exception as error:
    print(f'Ocurrio un Error: {error}')
finally:
    conexion.close()