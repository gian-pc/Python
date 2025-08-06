print('*** Sistema de Autenticacion ***')

USUARIO = 'gian'
PASS = '123'

usuario_input = input('USUARIO: ')
pass_input = input('PASSWORD: ')

usuario_correcto = usuario_input.strip() == USUARIO and pass_input.strip() == PASS

print(f'Usuario correcto: {usuario_correcto}')