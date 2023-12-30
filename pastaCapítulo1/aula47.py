palavra = 'perfume'
chute_user = ''
senha = '*******'
senha_nova = ''
posicao = 0
tentativas = 0

while True:
    chute_user = input('Digite uma letra (Apenas a primeira letra digitada será considerada): ').lower().strip()[0]
    posicao = 0
    tentativas += 1

    while True:
        try:
            
            if chute_user in palavra[posicao]:
                senha_nova = list(senha)
                senha_nova[posicao] = chute_user
                senha = ''.join(senha_nova)
                posicao += 1
                
            elif chute_user in palavra:
                posicao += 1
                pass
            else:
                posicao += 1
                pass
        except:
            print(senha)
                
            if True:
                break

    if senha == palavra:
        print('VOCÊ CONSEGUIU CHEGAR NA PALAVRA SECRETA, PARABÉNS!!!')
        print(f'A palavra era: {palavra}')
        print(f'Tentativas: {tentativas}')
        break