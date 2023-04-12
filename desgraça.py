duplicata = float(input('Digite o valor da sua duplicata: '))
diatraso = int(input('Quantos dias atrasou? '))
multa = duplicata + ( duplicata * 0.05 * diatraso)
print(f'Sua multa será de {multa:.3f}')