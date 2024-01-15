#Usei apenas para limpar o terminal na hora de escrever a lista
import os

lista = []

def escrever_lista():
    indices = range(len(lista))
    for posicao in indices:
        print(posicao, lista[posicao])

#Loop para a lista funcionar com os comandos desejados
while True:
    try:
        opcao = input('Selecione uma opção \n'
                    '[i]nserir [a]pagar [l]istar [p]arar: ').lower().strip()[0]
            
        if opcao == 'i':
            lista.append(input('Digite o que você deseja adicionar a lista: ').title().strip())

        elif opcao == 'a':
            apagar = int(input('Digite o número da lista que deseja apagar: '))
            del lista[apagar]
        
        elif opcao == 'l':
            os.system('cls')
            escrever_lista()
            if len(lista) == 0:
                print('Nada para listar')

        elif opcao == 'p':
            break
        
    except:
        print('Por favor, digite um índice da lista válido para apagar!')