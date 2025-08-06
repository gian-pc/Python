print('*** Generación Ticket de Venta ***')

precio_leche = float(input('Precio leche: '))
precio_pan = float(input('Precio pan: '))
precio_lechuga = float(input('Precio lechuga: '))
precio_platano = float(input('Precio platano: '))
descuento_porcentaje = int(input('Aplicar algún descuento (%)?: '))

# Calculo del subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga  + precio_platano

# Aplicar el descuento
descuento = subtotal * descuento_porcentaje/100

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# Calculo con impuestos (16%)
igv = subtotal_con_descuento * 0.16

# Calculo total de la compra (con impuestos)
total = subtotal_con_descuento + igv

print(f'''\nSubtotal: ${subtotal:.2f}
Descuento: ${descuento:.2f} ({descuento_porcentaje}%)
Subtotal con descuento: ${subtotal_con_descuento:.2f}
Impuesto (16%): ${igv:.2f}
Costo Total de la compra: ${total:.2f}''')
