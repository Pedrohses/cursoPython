def multiplic(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

numeros_teste = 2, 3, 5
multiplic_2_3_5 = multiplic(*numeros_teste)
print(multiplic_2_3_5)

###############################################

num = input('Digite um número: ')

def func_par_ou_impar():
    if int(num) % 2 == 0:
          return 'Par'
    return 'Ímpar'

# Outra possibilidade:
     
# def func_par_ou_impar():
#      return int(num) % 2 == 0

par_impar = func_par_ou_impar()
print(par_impar)

    