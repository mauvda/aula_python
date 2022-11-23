def semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terca',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sabado',
    }

    if dia == 7 or dia == 1:
        return dias.get(dia) + ' e fim de semana'
    elif dia not in range(1, 8):
        return dias.get(dia, 'Dia invalido')
    else:
        return dias.get(dia) + ' e dia de semana'


for i in range(8):
    print(semana(i))
