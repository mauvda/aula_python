#! python
with open('pessoas.csv') as arquivo:
    for run in arquivo:
        print('Nome: {}, Idade {}'.format(*run.strip().split(',')))

if arquivo.closed:
    print('Arquivos foi fechado')
