def receber_entrada() -> list:
    lista_nums = []
    for i in range(10):
        num = int(input('Informe um número: '))
        lista_nums.append(num)
    return lista_nums


def gerar_saida(lista_nums: list) ->list:
    saida = []
    for i in range(len(lista_nums)):
        if i % 2 == 0:
            saida.append(lista_nums[i] * 2)
        else:
            saida.append(lista_nums[i] * 3)
    return saida