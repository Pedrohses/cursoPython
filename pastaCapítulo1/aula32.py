# Exercício 1

num = input('Digite um número inteiro: ')

try:
    num_inteiro = int(num)
    sobra_de_divisao = num_inteiro % 2 == 0

    if sobra_de_divisao:
        print('O número é par')
    else:
        print('O número é ímpar')
except:
    print('Não é um número inteiro')

# Exercício 2

hora = input('Digite como número inteiro a hora que é agora: ')

try:
    hora_int = int(hora)
    hora_certa = hora_int < 25

    if hora_certa:
        bom_dia = hora_int >= 0 and hora_int <= 11
        boa_tarde = hora_int <= 17
        boa_noite = hora_int <= 23

        if bom_dia:
            print('Bom dia!')
        elif boa_tarde:
            print('Boa tarde!')
        elif boa_noite:
            print('Boa noite!')
    else:
        print('Digite uma hora válida')
except:
    print('Digite uma hora válida')

# Exercício 3

primeiro_nome = input('Digite seu primeiro nome: ')
quantidade_letras_nome = len(primeiro_nome)

nome_curto = quantidade_letras_nome <= 4
nome_normal = quantidade_letras_nome <= 6
nome_grande = quantidade_letras_nome > 6

if nome_curto:
    print('Seu nome é curto')
elif nome_normal:
    print('Seu nome é normal')
elif nome_grande:
    print('Seu nome é grande')