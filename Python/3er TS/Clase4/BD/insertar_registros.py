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
            sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUES (%s, %s, %s)'  # Placeholder

            valores = ('Carlos', 'Lara', 'cLara@gmail.com')  # Es una tupla
            cursor.execute(sentencia, valores)  # De esta manera ejecutamos la sentencia

            # conexion.commit(): esto se utiliza para guardar los cambios en la base de datos

            registros_instertados = cursor.rowcount  # Esto es para igresar columnas
            print(f'Los registros insertados son: {registros_instertados}')
except Exception as error:
    print(f'Ocurrio un Error: {error}')
finally:
    conexion.close()