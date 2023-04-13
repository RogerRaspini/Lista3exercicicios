clientisento = int(input('Digite o numero de clientes isentos de pendencias'))
clientemdia = int(input('digite o numero de clientes com as parcelas em dia'))
clientatrasado = int(input('digite o numero de clientes atrasados'))

total = clientatrasado + clientemdia + clientisento
porc1 = total/100 * clientisento
porc2 = total/100 * clientemdia
porc3 = total/100 * clientatrasado

print (f'{porc1} {porc2} {porc3}')
