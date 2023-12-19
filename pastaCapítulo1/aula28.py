nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
espaço = ' '

if nome != '' and idade != '':
    int_idade = int(idade)
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if espaço in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaço')
    print(f'Seu nome contém {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')