#! python
# from math import pi
import math
import sys


def formula(raio):
    return math.pi*float(raio)**2


def help():
    print('É necessário informar o Raio do circulo',
          '\nSintaxe: python', sys.argv[0], '<Raio>')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        # sys.exit(1)
    else:
        raio = sys.argv[1]
        area = formula(raio)
        print('Se o raio é', raio, 'entao a area é', "%.2f" % area)
