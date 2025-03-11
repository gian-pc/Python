
print('*** Generador de email ***')
nombre = 'Gian Paucar Cortez'
empresa = 'Global Mentoring'
dominio = '.com.pe'

nombre_normalizado = nombre.lower().replace(' ', '.')
print(f'Nombre usuario: {nombre}')
print(f'Nombre usuario normalizado: {nombre_normalizado}')
print()
print(f'Nombre empresa: {empresa}')
print(f'Extendion del dominio: {dominio}')

dominio_normalizado = '@'+empresa.lower().replace(' ', '') + dominio
print(f'Dominio de email normalizado: {dominio_normalizado}')

print()
print(f'Email final generado: {nombre_normalizado + dominio_normalizado}')