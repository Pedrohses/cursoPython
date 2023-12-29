# Calculadora com while
while True:
    try:
        num1 = input('Digite o primeiro número: ')
        num2 = input('Digite o segundo número: ')
        int_num1 = int(num1)
        int_num2 = int(num2)
        resultado = 0
        operador = input('Qual conta você deseja realizar? adição[1] subtração [2] multiplicação[3] divisão[4]: ').strip()[0]

        if operador == '1':
            resultado = int_num1 + int_num2
            print(resultado)
        elif operador == '2':
            resultado = int_num1 - int_num2
            print(resultado)
        elif operador == '3':
            resultado = int_num1 * int_num2
            print(resultado)
        elif operador == '4':
            resultado = int_num1 / int_num2
            print(resultado)
        else:
            print('Digite o número equivalente a um operador válido')

        continuar_ou_sair = input('Deseja continuar? Sim[s] ou Não[n]: ').lower().strip()[0]

        while continuar_ou_sair == 's':
            num3 = input('Digite o número que irá fazer a conta com o resultado: ')
            int_num3 = int(num3)
            operador = input('Qual conta você deseja realizar? adição[1] subtração [2] multiplicação[3] divisão[4]: ').strip()[0]

            if operador == '1':
                resultado += int_num3
                print(resultado)
            elif operador == '2':
                resultado -= int_num3
                print(resultado)
            elif operador == '3':
                resultado *= int_num3
                print(resultado)
            elif operador == '4':
                resultado /= int_num3
                print(resultado)
            else:
                print('Digite o número equivalente a um operador válido')

            continuar_ou_sair = input('Deseja continuar? Sim[s] ou Não[n]: ').lower().strip()[0]
        reiniciar = input('Deseja reiniciar? Sim[s] ou Não[n]: ').lower().strip()[0]
        if reiniciar == 'n':
            print('Obrigado por usar a calculadora!')
            break
    except:
        print('Um dos valores digitados não é um número')
        reiniciar = input('Deseja reiniciar? Sim[s] ou Não[n]: ').lower().strip()[0]
        if reiniciar == 'n':
            print('Obrigado por usar a calculadora!')
            break