import time

print('-=-' * 15) 

num = int(input(' Dgite até que número você quer que o contador conte: '))

for c in range(1, num + 1):
    print(f' Contador: {c}')
    time.sleep(1)

print('-=-' * 15) 