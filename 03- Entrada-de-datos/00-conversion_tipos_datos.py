# conversion de tipos de datos

# Convertir de cadena a número
numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'Cadena a entero: {numero_entero} y es de tipo: {type(numero_entero)}')

# Convertir de cadena a flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print(f'Cadena a flotante: {numero_flotante} y es de tipo: {type(numero_flotante)}')

# Convertir de numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Numero a cadena:  {numero_cadena} y es de tipo: {type(numero_cadena)}')

# Convertir a booleano
# Tipo bool es Falso en los siguientes casos:

# Regresa False --> Si el valor es 0, cadena vacia, None
numero_entero = 0
booleano = bool(numero_entero)
print(f'Valor booleano de 0: {booleano}')

cadena = ''
booleano = bool(cadena)
print(f'Valor booleano de cadena vacía: {booleano}')

variable = None
booleano = bool(variable)
print(f'Valor booleano de None: {booleano}')

# Regresa True --> Si el valor es distinto de 0, None y cadena vacía
numero_entero = 5
booleano = bool(numero_entero)
print(f'Valor booleano de 5: {booleano}')

cadena = 'Hola'
booleano = bool(cadena)
print(f'Valor booleano de cadena No vacía: {booleano}')
