print('*** Bienvenidos al Sistema Bancario ***')

# Ingreso de respuesta
salir_sistema = input('Desea salir del sistema?: ')

# Limpiar y validar condición
salir_sistema = salir_sistema.strip().lower() == 'si'

# Mostrar
if not salir_sistema:
    print('Continuamos dentro del sistema')
else:
    print('Salimos del sistema')
