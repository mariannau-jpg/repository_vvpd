import numpy as np
from random import randint


def get_size():
    lines, columns = input('Введите размеры массива: ').split()
    print(f'Введён размер массива {lines} на {columns}')
    return int(lines), int(columns)


def manual_input(size):
    array_manual_input = np.zeros(size, dtype=int)
    for i in range(size[0]):
        for j in range(size[1]):
            elem = int(input('Введите элемент массива: '))
            array_manual_input[i, j] = elem
            print(f'Введён элемент {i} {j}: {elem}')
    return array_manual_input


def automatic_input(size):
    array_automatic_input = np.zeros(size, dtype=int)
    for i in range(size[0]):
        for j in range(size[1]):
            elem = randint(0, 100)
            array_automatic_input[i, j] = elem
    return array_automatic_input


size = get_size()
command = int(input('''Для создания массива выберите режим:
1. Вручную
2. Автоматически
3. Назад
0. Выйти из программы
'''))
while command != 0:
    if command == 1:
        matrix = manual_input(size)
        print(matrix)
        break
    elif command == 2:
        matrix = automatic_input(size)
        print(matrix)
        break
    elif command == 3:
        size = get_size()
    command = int(input('''Для создания массива выберите режим:
1. Вручную
2. Автоматически
3. Назад
0. Выйти из программы
'''))
