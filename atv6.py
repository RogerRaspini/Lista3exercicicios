valorconta = int(input('digite o valor da conta:' ))
valorpago = int(input('Digite o valor pago: '))



troco = abs(valorconta - valorpago)
print(troco)

notascentena = int(troco/100)
notasdezena = int(troco/10) - (10*notascentena)
notasunidade = int(troco) - (100*notascentena) - (10*notasdezena)



print(f'serão necessarias {notascentena:.0f} notas de 100')
print(f'serão necessarias {notasdezena:.0f} notas de 10')
print(f'serão necessarias {notasunidade} notas de 1')
