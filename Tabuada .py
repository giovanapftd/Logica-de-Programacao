num = float(input('De qual número você quer saber a tabuada: '))
print(f'-=-=-=- TABUADA DO NÚMERO {num:.0f} -=-=-=-')

for c in range(1, 11):
    tabuada = num * c
    print(f' {num:.0f} x {c} = {tabuada:.0f}')
print('-=-' * 12)