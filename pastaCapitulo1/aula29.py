numero_str = input(
    'Vou dobrar o número que você digitar: '
)

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')



# numero_float = float(numero_str)
# if numero_str.isdigit():
#     print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')