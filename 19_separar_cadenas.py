# Separar cadenas (split)

datos = 'Hola Mundo'
lista = datos.split(' ') # por defecto separa por espacios
print(lista) # ['Hola', 'Mundo']

datos = 'Juan,30,Perú'
lista = datos.split(',') # separa por comas
print(lista) # ['Juan', '30', 'Perú']