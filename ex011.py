larg = float(input('Qual é a largura da sua parede?'))
alt = float(input('Qual é a altura da sua parede?'))

area = larg*alt
print('A largura de {}m, mais a altura {}m é igual a {}m²'.format(larg, alt, area))
tinta = area/2

print('Voce precisara de {}l de tinta'.format(tinta))

