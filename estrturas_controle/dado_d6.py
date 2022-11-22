from random import randint


def sortear_dado():
    return randint(1, 6)


if __name__ == '__main__':
    cont = 0
    while cont != 1:
        aposta = sortear_dado()
        for dado in range(1, 7):
            if dado % 2 == 1:
                continue

            if dado == aposta:
                print("Acertou!\nO valor e: ", aposta)
                cont = 1
                break

        else:
            print("Nao houve acertos")
