string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = "Python", 'é', 'legal'

salas = [
    ['Maria', 'Helena'],

    ['Elaine', ],

    ['Luiz', 'João', 'Eduarda'],
]


# p, b, *_, ap, u = lista
# print(p, u, ap)

# for nome in lista:
#     print(nome, end=' ')
# print(*lista)
# print(*string)

print(*salas, end='\n')
print(*salas, sep='\n')