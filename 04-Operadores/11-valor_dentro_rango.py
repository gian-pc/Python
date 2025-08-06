print('*** Valor dentro de Rango ***')

# Declaramos Min y Max
MINIMO = 0
MAXIMO = 5

# Ingreso de datos
dato = int(input(f'Ingrese un número entre {MINIMO} y {MAXIMO}: '))

# Verificamos si el número esta dentro del rango
dentro_de_rango = MINIMO <= dato <= MAXIMO

# Mostramos en pantalla
print(f'El numero {dato} esta dentro del rango: {dentro_de_rango}')