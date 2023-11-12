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
            sentencia = 'UPDATE persona SET nombre= %s, apellido= %s, email=%s WHERE id_persona = %s'
            valores = (
                ('Juan', 'Porsel', 'Jporsel@gmail.com', 11),
                ('Leonel', 'Cano', 'leocano@gmail.com', 10),
                ('Facundo', 'Arana', 'facuara@gmail.com', 12),

            )  # Es una tupla de tuplas

            cursor.executemany(sentencia, valores)  # executemany agrega los nuevos registros y los guarda

            registros_actualizados = cursor.rowcount  # Esto es para igresar columnas
            print(f'Los registros fueron actulizados : {registros_actualizados}')

except Exception as error:
    print(f'Ocurrio un Error: {error}')
finally:
    conexion.close()