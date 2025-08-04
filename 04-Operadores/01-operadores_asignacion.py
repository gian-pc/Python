# Operadores de Asignacion

# Asignación simple
numero = 5
print(f'Asignación simple: {numero}')

# Asignación multiple
a, b, c = 'Hola', 2, 9.3
print(f'Asignación multiple: a={a}, b={b}, c={c}')

# Asignación encadenada
contador_1 = contador_2 = 0
print(f'Asignación encadenada: contador_1={contador_1}, contador_2={contador_2}')

# Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'Valores iniciales x={x}, y={y}')

# Aplicando el concepto de asignación multiple, intercambiamos valores
x, y = y, x
print(f'Valores iniciales x={x}, y={y}')

# Recibir multiples valores de la entrada del usuario
nombre, apellido = input('Ingresa tu nombre y apellido separador por coma: ').split(',')
print(f'Nombre: {nombre.strip()}, Apellido: {apellido.strip()}')