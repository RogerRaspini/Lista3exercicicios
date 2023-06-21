# def calcular_fatorial(num: int) -> int:
#    result = 1
#    for i in range(1, num+1):
#        result *= i
#   return result

#RECURSIVIDADE ¬
def calcular_fatorial(num:int) -> int:
    if num == 1:
        return 1

    return num * calcular_fatorial(num-1)

def calcular_arranjos(n:int, p:int)->float:
    return calcular_fatorial(n) / calcular_fatorial(n-p)

def calcular_combinaçoes(n:int,p:int)->float:
    return calcular_fatorial(n) / calcular_fatorial(p) * (calcular_fatorial(n-p))

def obter_opcao() -> int:
    print('**Menu de Opções **\n'
          '1-Calcular Combinação\n'
          '2-Calcular Arranjo\n'
          '3-Sair')
    return int(input('==>'))


#8) Desenvolva um programa que permita ao usuário realizar o cálculo de arranjos e
#combinações. O programa deverá exibir ao usuário um menu com 3 opções, conforme abaixo:
#1 – Calcular Combinação
#2 – Calcular Arranjo
#3 – Sair
#Informe a opção desejada:
#Este menu deve ser exibido após cada cálculo do usuário, e deverá ser exibido novamente até
#o usuário solicitar a opção sair.


def tratar_combinacoes():
    n = int(input('Informe o número de elementos (N): '))
    p = int(input('Infomre o número de agrupamentos (P): '))
    result = calcular_combinaçoes(n,p)
    print(f'O total de combinações é {result:.1f}')

def tratar_arranjos():
    n = int(input('Informe o número de elementos (N): '))
    p = int(input('Infomre o número de agrupamentos (P): '))
    result = calcular_arranjos(n,p)
    print(f'O total de arranjos é {result:.1f}')



