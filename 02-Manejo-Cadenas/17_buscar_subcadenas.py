# Buscar subcadenas

cadena = 'Hola, mundo! mundo mundo'
indice = cadena.find('mundo')
print(f'Indice de la subcadena mundo: {indice}')  # 6

# Obtener el indice de la subcadena de Hola
indice = cadena.find('hola')
print(f'Indice de la subcadena hola: {indice}')  # -1 --> No se encuentró la subcadena