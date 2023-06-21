pessoas = ['João', 'Pedro','Jorge','Afonso']

print(pessoas[0])

print(len(pessoas))
for i in range(len(pessoas)):
    print(pessoas[i])
print()
print()
print()

for p in pessoas:
    print(p)

for (i,p) in enumerate(pessoas):
    print(f'Nome: {p} na posição: {i}')

