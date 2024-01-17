lista = ['Maria', 'Helena', 'Pedro']
lista.append('João')

lista_enumerada = list(enumerate(lista))

# for item in lista_enumerada:
#     indice, nome = item
#     print(indice, nome)

for indice, nome in lista_enumerada:
    print(indice, nome)
    
# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
