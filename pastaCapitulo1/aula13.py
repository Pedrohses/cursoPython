nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura em metros: '))
peso = int(input('Digite seu peso em quilos: '))
imc = peso/(altura*altura)

print(f'{nome} tem altura de {altura:.2f}, pesa {peso} quilos e seu IMC é: {imc:.2f}')