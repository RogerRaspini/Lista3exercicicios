parcelaspagas = int(input('Quantas parcelas foram pagas do consórcio?: '))
totalparcelas = 24
valorparcelas = 1000
totalpago = parcelaspagas * valorparcelas
otantoquefalta = totalparcelas - parcelaspagas
saldodevedor = otantoquefalta * 1000
print (f'Voce pagou {totalpago} R$, e deve {otantoquefalta} parcelas, no valor de {saldodevedor} R$')