from math import sin, cos, tan, radians
angulo = float(input('Entre com um angulo'))

seno = sin(radians(angulo))
print('O seno de {} é {:.2f}'.format(angulo,seno))

cosseno = cos(radians(angulo))
print('O cosseno de {} é {:.2f}'.format(angulo,cosseno))

tangente = tan(radians(angulo))
print('A tangente de {} é {:.2f}'.format(angulo,tangente))

