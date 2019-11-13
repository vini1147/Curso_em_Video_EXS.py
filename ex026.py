nome = str(input('Digite algo')).upper().strip()
print('A letra A aparece {} vezes'.format(nome.count('A')))
print('A primeira letra A está na posição {}'.format(nome.find('A')+1))
print('A ultima letra A  está na posição {}'.format(nome.rfind('A')+1))
