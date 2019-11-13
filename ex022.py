nome = str(input('Digite seu nome')).strip()

print('Seu nome em maiusculo é {}:'.format(nome.upper()))

print('Seu nome em minusculo é {}:'.format(nome.lower()))

sp = nome.split()
print('''Seu nome completo sem os espacos tem o
total de: {} letras'''.format(len(''.join(sp))))

print('''Outro metodo de contar sem
os espacos, {} letras'''.format(len(nome)-nome.count(' ')))

print('O seu primeiro nome tem {} letras'.format(len(sp[0])))
