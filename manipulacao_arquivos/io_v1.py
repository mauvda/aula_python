#! python
arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()


for run in dados.splitlines():
    print('Nome: {}, Idade {}'.format(*run.split(',')))
