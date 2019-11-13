from random import randint
from time import sleep
print('(=====)'*6)
print('Estou sorteando um numero para voce jogar')
print('(=====)'*6)
n = int(input('Digite um numero de 0 a 5: '))
ran = randint(0, 5)
print('Processando...')
sleep(5)
if n == ran:
    print('Parabens, voce digitou {} e o numero sorteado foi {}'.format(n, ran))
else:
    print('Infelizmente voce errou, numero sorteado foi {} e voce chutou o {}'.format(ran, n))


