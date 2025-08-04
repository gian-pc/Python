print('*** Sistema Descuento VIP ***')

nro_productos_descuento = 10
cantidad_productos = int(input('cuantos productos compraste hoy? '))
tiene_membresia = input('Tienes la membresía de la tienda (Si/No)? ')

tiene_descuento = cantidad_productos >= nro_productos_descuento and tiene_membresia.strip().lower() == 'si'
print(f'Tienes descuento?: {tiene_descuento}')