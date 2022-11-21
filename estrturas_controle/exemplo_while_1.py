from random import randint

numero_info = -1
numero_secreto = randint(0, 9)

while numero_info != numero_secreto:
    numero_info = int(input('Informe um numero de 0 a 9: '))

print('O numero secreto é', numero_info)