print('*** Sistema Prestamo de Libros ***')

DISTANCIA_PERMITIDA_KM = 3
tiene_credencial = input('Cuentas con credencial de estudiante (Si/No)? ')
distancia_biblioteca_km = int(input('A cuanto km vives de la biblioteca? '))

es_elegible_prestamo = tiene_credencial.strip().lower() == 'si' or distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM
print(f'Eres elegible prestamo: {es_elegible_prestamo}')

print('hola')