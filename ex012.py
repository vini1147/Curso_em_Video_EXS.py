p = float(input('Digite o valor da mercadoria para obter o desconto'))

pd = ((p*5)/100)
print('O preco atual de {}R$ teve o valor de desconto {:.2f}R$'.format(p, pd))

print('Valor final ficou {}R$ '.format(p-pd))
