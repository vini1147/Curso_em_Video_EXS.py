salario = float(input('Qual é o seu salario? R$'))
novo= salario + (salario*15)/100

print('Seu salario era R${:.2f}, com reajuste está R${:.2f}'.format(salario, novo))
