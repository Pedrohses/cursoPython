frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossun.'.lower()

letra_que_apareceu_mais_vezes = ''
qntd_mais_vezes = 0
i = 0

while i < len(frase):
    letra_atual = frase[i]
    qntd_atual = frase.count(letra_atual)

    # Só para pular os espaços
    if ' ' in letra_atual:
        i += 1
        continue
    
    #Para atribuir o valor da letra que aparece mais vezes e quantas vezes aparece para as variáveis certas
    if qntd_atual > qntd_mais_vezes:
        qntd_mais_vezes = qntd_atual
        letra_que_apareceu_mais_vezes = letra_atual

    i += 1

print(f'A letra "{letra_que_apareceu_mais_vezes}" apareceu "{qntd_mais_vezes}" sendo assim a letra que mais apareceu')
    