vel = float(input('Em que velocidade está o carro?'))

if vel > 80:
    multa = (vel-80)*7
    print('voce foi multado, o valor é: {:.2f} reais'.format(multa))
else:
    print('voce nao foi multado')
