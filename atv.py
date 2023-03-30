qtd = int(input('Digite o quantos produtos voce comprou: '))
preço = float(input('Digite o preço do produto: '))
desc = float(input('Digite a porcentagem de desconto: '))
valores = qtd * preço
des = (100 - desc)
tudo = (valores / 100) * des
valorsemdesc = valores - tudo

print('o valor total com o desconto fica: ' , tudo , 'R$')
print('o valor total sem os descontos fica: ' , valores , 'R$')
print('o valor do desconto é' , valorsemdesc , 'R$' )

