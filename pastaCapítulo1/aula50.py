lista = ['Maria', 'Helena', 'Pedro']
lista.append('João')

indices = range(len(lista)) #range pega o tamanho de 0 até o final

for posicao in indices:
    print(posicao, lista[posicao])