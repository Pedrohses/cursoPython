primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

if int_primeiro_valor > int_segundo_valor:
    print('O primeiro valor é maior')
elif int_primeiro_valor < int_segundo_valor:
    print('O segundo valor é maior')
else:
    print('Os dois valores são iguais')