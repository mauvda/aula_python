#! python
# from math import pi
import math
import sys


def formula(raio):
    return math.pi*float(raio)**2


if __name__ == '__main__':
    raio = sys.argv[1]
    area = formula(raio)
    print('Se o raio é', raio, 'entao a area é', "%.2f" % area)
