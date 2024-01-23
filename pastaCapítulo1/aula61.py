cpf = '459.552.528-19'

# Remove os caracteres que não são números da string CPF
REMOVEDOR_DE_CARACTERES = '.-'

for i in range(0,len(REMOVEDOR_DE_CARACTERES)):
    cpf = cpf.replace(REMOVEDOR_DE_CARACTERES[i],'')

num_cpf = int(cpf)
num_cpf = list(cpf)

# separar os 9 primeiros digitos dos 2 últimos
nove_primeiros_digitos_cpf = []
dois_ultimos_digitos_cpf = []
digitos = 0

while digitos <= 8:
    nove_primeiros_digitos_cpf.append(int(num_cpf[digitos]))
    digitos += 1


while digitos <= 10:
    dois_ultimos_digitos_cpf.append(int(num_cpf[digitos]))
    digitos += 1

# Cálculo do primeiro dígito do CPF
regressiva = 10
primeiros_digitos_multiplicados = 0

for contagem in range(len(nove_primeiros_digitos_cpf)):
    primeiros_digitos_multiplicados += nove_primeiros_digitos_cpf[contagem] * regressiva
    regressiva -= 1

primeiros_digitos_multiplicados *= 10
primeiro_digito_cpf = primeiros_digitos_multiplicados % 11

if primeiro_digito_cpf > 9:
    primeiro_digito_cpf = 0
else:
    pass

print(primeiro_digito_cpf)


