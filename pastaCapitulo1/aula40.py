# Calculadora com while
while True:
    try:
        num1 = input('Digite o primeiro número: ')
        num2 = input('Digite o segundo número: ')
        float_num1 = float(num1)
        float_num2 = float(num2)
        resultado = 0
        operador = input('Qual conta você deseja realizar? adição[1] subtração [2] multiplicação[3] divisão[4]: ').strip()[0]

        if operador == '1':
            resultado = float_num1 + float_num2
            print(f'{num1} + {num2} = {resultado}')
        elif operador == '2':
            resultado = float_num1 - float_num2
            print(f'{num1} - {num2} = {resultado}')
        elif operador == '3':
            resultado = float_num1 * float_num2
            print(f'{num1} * {num2} = {resultado}')
        elif operador == '4':
            resultado = float_num1 / float_num2
            print(f'{num1} / {num2} = {resultado}')
        else:
            print('Digite o número equivalente a um operador válido')

        continuar_ou_sair = input('Deseja continuar? Sim[s] ou Não[n]: ').lower().strip()[0]

        while continuar_ou_sair == 's':
            num3 = input('Digite o número que irá fazer a conta com o resultado: ')
            float_num3 = float(num3)
            operador = input('Qual conta você deseja realizar? adição[1] subtração [2] multiplicação[3] divisão[4]: ').strip()[0]
            resultado2 = 0

            if operador == '1':
                resultado2 = resultado + float_num3
                print(f'{resultado} + {float_num3} = {resultado2}')
                resultado = resultado2
            elif operador == '2':
                resultado2 = resultado - float_num3
                print(f'{resultado} - {float_num3} = {resultado2}')
                resultado = resultado2
            elif operador == '3':
                resultado2 = resultado * float_num3
                print(f'{resultado} * {float_num3} = {resultado2}')
                resultado = resultado2
            elif operador == '4':
                resultado2 = resultado / float_num3
                print(f'{resultado} / {float_num3} = {resultado2}')
                resultado = resultado2
            else:
                print('Digite o número equivalente a um operador válido')

            continuar_ou_sair = input('Deseja continuar? Sim[s] ou Não[n]: ').lower().strip()[0]
        reiniciar = input('Deseja reiniciar os números do 0? Sim[s] ou Não[n]: ').lower().strip()[0]
        if reiniciar == 'n':
            print('Obrigado por usar a calculadora!')
            break
    except:
        print('Um dos valores digitados não é um número!')
        reiniciar = input('Deseja reiniciar os números do 0? Sim[s] ou Não[n]: ').lower().strip()[0]
        if reiniciar == 'n':
            print('Obrigado por usar a calculadora!')
            break