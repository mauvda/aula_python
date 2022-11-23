#! python


# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == '__main__':
    # Listar os 301 primeiros numeros da sequencia de fibonacci
    for fib in fibonacci(301):
        print(fib, end=', ')
