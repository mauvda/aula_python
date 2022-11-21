import sys

nota = float(sys.argv[1])

if __name__ == '__main__':

    if nota > 10 or nota < 0:
        print('A Nota deve ser menor que 10 e maior que zero')
        sys.exit()

    if nota >= 9.1:
        print('Conceito A')
        sys.exit()

    if nota >= 8.1 and nota <= 9:
        print('Conceito A-')
        sys.exit()

    if nota >= 7.1 and nota <= 8:
        print('Conceito B')
        sys.exit()

    if nota >= 6.1 and nota <= 7:
        print('Conceito B-')
        sys.exit()

    if nota >= 5.1 and nota <= 6:
        print('Conceito C')
        sys.exit()

    if nota >= 4.1 and nota <= 5:
        print('Conceito C-')
        sys.exit()

    if nota >= 3.1 and nota <= 4:
        print('Conceito D')
        sys.exit()

    if nota >= 2.1 and nota <= 3:
        print('Conceito D-')
        sys.exit()

    if nota >= 1.1 and nota <= 2:
        print('Conceito E')
        sys.exit()

    if nota >= 0 and nota <= 1:
        print('Conceito E-')
        sys.exit()
