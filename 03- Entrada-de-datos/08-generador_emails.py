print('*** Sistema Generador de Emails ***')

nombre = input('Cual es tu nombre?: ')
apellidos = input('Cuales son tus apellidos?: ')
empresa = input('Cual es el nombre de tu empresa?: ')
dominio = input('Cual es el dominio de tu empresa?: ')

# Normalizacion de datos recibidos
nombre = nombre.strip().lower().replace(' ', '.')
apellidos = apellidos.strip().lower().replace(' ', '.')
empresa = empresa.strip().lower().replace(' ', '')
dominio = dominio.strip().lower().replace(' ', '')

# Generar el email
email = f'{nombre}.{apellidos}@{empresa}{dominio}'

# Mostramos en pantalla
print(f'''
Tu nuevo email generado por el sistema es:
    {email}
    Felicidades!
''')