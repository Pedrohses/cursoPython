cpf = '460.509.858-55'

# Remove os caracteres que não são números da string CPF
REMOVEDOR_DE_CARACTERES = '.-'

for i in range(0,len(REMOVEDOR_DE_CARACTERES)):
    cpf = cpf.replace(REMOVEDOR_DE_CARACTERES[i],'')

# Separar os 9 primeiros dígitos do CPF
nove_num_cpf = cpf[:9]

# Cálculo do primeiro dígito do CPF
regressiva = 10
primeiros_digitos_multiplicados = 0

for contagem in nove_num_cpf:
    primeiros_digitos_multiplicados += int(contagem) * regressiva
    regressiva -= 1

primeiro_digito_cpf = (primeiros_digitos_multiplicados * 10) % 11

if primeiro_digito_cpf > 9:
    primeiro_digito_cpf = 0
else:
    pass

print(primeiro_digito_cpf)