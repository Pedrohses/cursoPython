nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura em metros: '))
peso = int(input('Digite seu peso em quilos: '))
imc = peso/(altura*altura)

print(nome, 'tem', altura, 'de altura, pesa', peso, 'quilos e seu IMC é: ', imc )