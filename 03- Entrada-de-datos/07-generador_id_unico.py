from random import randint

print('*** Sistema Generador de ID Unico ***')

nombre = input('Cual es tu nombre?: ')
apellido = input('Cual es tu apellido?: ')
fecha_nacimiento = input('Cual es tu fecha nacimiento? (YYYY): ')

# Normalizar los valores
nombre_2 = nombre.strip().upper()[0:2]  # strip quita espacios al inicio o al final
apellido_2 = apellido.strip().upper()[0:2]
fecha_nacimiento_2 = fecha_nacimiento.strip()[2:]  # También puede  ser [2:4]

# Generar el valor aleatorio de 4 cifras
num_aleatorio = randint(1000, 9999)

# Generamos el valor de id unico
id_unico = f'{nombre_2}{apellido_2}{fecha_nacimiento_2}{num_aleatorio}'

# Mostramos en pantalla
print(f'''\nHola {nombre},
    Tu nuevo número de identificación (ID) generado por el sistema es:
    {id_unico}
    Felicidades!
    ''')
