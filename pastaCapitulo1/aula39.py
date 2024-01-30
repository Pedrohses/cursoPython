nome = input('Digite seu nome: ')
tamanho_nome = len(nome)
num_da_letra = 0
nova_string = ''

while True:
    nova_string += ('*' + nome[num_da_letra])
    num_da_letra += 1

    if num_da_letra >= tamanho_nome:
        nova_string += '*'
        print(nova_string)
        break

    # RESOLUÇÃO DO PROFESSOR
# nome = 'Luiz Otávio'
# indice = 0
# novo_nome = ''

# while indice < len(nome):
#     letra = nome[indice]
#     novo_nome += f'*{letra}'
#     indice += 1

# novo_nome += '*'    
# print(novo_nome)