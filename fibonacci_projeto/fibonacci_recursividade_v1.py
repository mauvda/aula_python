#! python


# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
def fibonacci(quantidade, resultado=(0, 1)):
    if quantidade == len(resultado):
        return resultado
    return fibonacci(quantidade, resultado + (sum(resultado[-2:]),))


if __name__ == '__main__':
    # Listar os 301 primeiros numeros da sequencia de fibonacci
    for fib in fibonacci(20):
        print(fib, end=', ')
