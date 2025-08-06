print('*** Aplicación de Salud y Fitness ***')

# Constantes
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04

# Ingreso de datos
nombre = input('Cual es tu nombre? ')
pasos = int(input('Cuantos pasos has caminado hoy? '))


# Meta de pasos diarios
meta_pasos = 'Si' if pasos >= META_PASOS_DIARIOS else 'No'

# Kcal quemadas
calorias_quemadas = pasos * CALORIAS_POR_PASO

# Mostramos en pantalla
print(f'\nUsuario: {nombre}')
print(f'Meta a alcanzar : {META_PASOS_DIARIOS} pasos')
print('-------------------------------')
print(f'Pasos dados hoy: {pasos}')
print(f'Calorias quemadas hoy: {calorias_quemadas} kcal')

print(f'Cumplio la meta?: {meta_pasos}')



