#! python
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for run in arquivo:
            pessoa = run.strip().split(',')
            print('Nome: {}, Idade {}'.format(*pessoa), file=saida)

if arquivo.closed and saida.close:
    print('Arquivos foi fechado')
