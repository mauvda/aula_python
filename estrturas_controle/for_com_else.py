PLAVRAS_PROIBIDAS = (
    'politica', 'futebol', 'religiao'
)

textos = ['Joao gosta de futebol e politica',
          'A praia e divertida']


for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PLAVRAS_PROIBIDAS:
            print('Texto possoi palavras proibidas', palavra)
            break
    else:
        print('Texto autorizado:', texto)
