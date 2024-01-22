frase = '   Olha só que   , coisa interessante             '
# o método split serve para quebrar ou nos espaços ou onde eu der como referência transformando numa lista 
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
# O método strip serve para retirar os espaços
    lista_frases.append(lista_frases_cruas[i].strip()) 

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = '-'.join('abc')
print(frases_unidas)