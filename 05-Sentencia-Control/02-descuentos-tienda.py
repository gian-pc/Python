print('*** Descuento Tienda ***')

monto = input('Ingrese el monto de su compra: $ ')
miembro = input('Es miembro de la tienda (Si/No)?: ')

# Limpiamos y convertimos datos
monto = float(monto)
miembro = miembro.strip().lower()

# Calculamos Descuentos
if monto > 1000 and miembro == 'si':  # Compra > 1000 y Si es miembro --> Descuento 10%
    descuento = monto * 0.10
    porcentaje = 10

elif miembro == 'si':  # Si solo es miembro --> Descuento 5%
    descuento = monto * 0.05
    porcentaje = 5

else:  # Si no es miembro y no compro más de 1000 --> Descuento 0%
    descuento = 0
    porcentaje = 0

# Calculamos el monto total a pagar
monto_final = monto - descuento

# Mostramos resultados
if porcentaje > 0:
    print(f'\n😂Felicidades, has obtenido un descuento del {porcentaje}%')
else:
    print('\n😒 No obtuviste ningún tipo de descuento')
    print('Te invitamos a hacerte miembro de la tienda')

print('------------------------------------------------')
print(f'Monto de la compra: $ {monto}')
print(f'Monto del descuento: $ {descuento}')
print('------------------------------------------------')
print(f'Monto final de la compra con descuento: $ {monto_final}')
print('------------------------------------------------')
