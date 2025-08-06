print('*** Revisión Valor Positivo ***')

numero = int(input('Ingresa un numero: '))

if numero > 0:
    print(f'Es positivo: {numero}')
elif numero < 0:
    print(f'Es negativo: {numero}')
else:
    print(f'Es cero {numero}')