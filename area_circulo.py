#! python
import math
import sys
import errno


def formula(raio):
    return math.pi*float(raio)**2


def help():
    print('É necessário informar o Raio do circulo',
          '\nSintaxe: python', sys.argv[0], '<Raio>')


def is_float(valor):
    try:
        float(valor)
    except ValueError:
        return False

    return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric() and not is_float(sys.argv[1]):
        help()
        print('\nO vaor do raio deve ser um número\n')
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = formula(raio)
    print('Se o raio é', raio, 'entao a area é', "%.2f" % area)
