#! python
# from math import pi
import math

raio = input('Informe o raio: ')
formula = math.pi*float(raio)**2
if __name__ == '__main__':
    print('Se o Raio e igual a', raio,
          '\nEntao a area total',
          'do circulo e igual a', "%.2f" % formula)
