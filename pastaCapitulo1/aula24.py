#nome = 'Pedro'
#print(nome[2])
#print('e' in nome)
#print('j' in nome)
#print('Ped' in nome)
#print(10 * '-' )
#print('e' not in nome)
#print('j' not in nome)
#print('Ped' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite a letra que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

