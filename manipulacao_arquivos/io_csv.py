#! python
import csv

try:
    with open('desafio-ibge.csv') as arquivo:
        with open('ibge.txt', 'w') as escrita:
            for run in csv.reader(arquivo):
                print('Nome de Origem: {} e Nome de destino: {}'.format(
                      *run[3].strip().split(','),
                      *run[8].strip().split(',')), file=escrita)
finally:
    if arquivo.closed and escrita.closed:
        print('Arquivo fechado')
