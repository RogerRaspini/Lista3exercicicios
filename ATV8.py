clientes = int(input('Diga quantos clientes tem isentos de pendencias: '))
clientes2 = int(input('Diga quantos clientes tem com parcelas em dia: '))
clientes3 = int(input('Diga quantos clientes tem com parcelas em atraso: '))

total = clientes+clientes3+clientes2
porc1 = clientes*100 / total
porc2 = clientes2*100 / total
porc3 = clientes3*100 / total

print (f'A porcentagem de clientes isentos são: {porc1:.2f} %')
print (f'A porcentagem de clientes com parcelas em dia são: {porc2:.2f} %')
print (f'A porcentagem de clientes com parcelas em atraso são: {porc3:.2f} %')

