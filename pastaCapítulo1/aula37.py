contador = 0
teste = 0

while contador <= 40:
    contador += 1
    
    if contador == 6:
        print('Não vou mostrar o 6.')
        continue
    
    if contador >= 10 and contador <= 27:
        print(f'Não vou mostrar o {contador}')
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')