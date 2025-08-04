#  Inmutabilidad en cadenas

cadena1 = 'Hola Mundo'
# cadena1[0] = 'h' # Error --> No podemos modificar los caracteres de una cadena
cadena2 = cadena1 # cadena2 apunta a la misma direccion de memoria que cadena1
cadena1 = 'Adios'
print(cadena1)
print(cadena2)

# Por lo tanto ninguno es candidato para el recolector de basura