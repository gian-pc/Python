print('*** Generación Ticket de Venta ***')

precio_leche = float(input('Precio leche: '))
precio_pan = float(input('Precio pan: '))
precio_lechuga = float(input('Precio lechuga: '))
precio_platano = float(input('Precio platano: '))

subtotal = precio_leche + precio_pan + precio_lechuga  + precio_platano
igv = subtotal * 0.16
total = subtotal + igv

print(f'''\nSubtotal: ${subtotal:.2f}
Impuesto (16%): ${igv:.2f}
Costo Total de la compra: ${total:.2f}''')
