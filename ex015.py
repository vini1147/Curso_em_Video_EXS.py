km = float(input('Quantos km foi pecorrido com esse carro? KM'))
dias = int(input('Quantos dias ele ficou alugado?'))
preco = (60*dias) + (0.15*km)

input('O preco total ficou de R${:.2f}'.format(preco))
