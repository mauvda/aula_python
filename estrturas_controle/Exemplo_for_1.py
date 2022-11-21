#! python
def medidor(valor):
    if 0 <= valor < 18:
        return 'Voce e menor de valor'
    elif valor in range(18, 64):
        return 'Voce e adulto'
    elif valor in range(65, 100):
        return 'Voce e idoso'
    elif valor >= 100:
        return 'voce e centenario'
    else:
        return 'Idade invalida'


if __name__ == '__main__':
    for idade in (17, 35, 87, 113, -2):
        print(f'{idade}: {medidor(idade)}')
