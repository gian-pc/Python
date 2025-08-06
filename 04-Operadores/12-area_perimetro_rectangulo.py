print('*** Calculo Area y Perimetro de un Rectangulo ***')

base = float(input(f'Ingrese la base de la rectangulo: '))
altura = float(input(f'Ingrese la altura de la rectangulo: '))

# Realizamos el calculo
area = base * altura
perimetro = (base + altura) * 2

# Mostramos en pantalla
print(f'Area del Rectangulo: {area}')
print(f'Perimetro del Rectangulo: {perimetro}')