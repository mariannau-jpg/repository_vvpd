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
print('Вас приветствует программа для работы с двумерными массивами!')
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
if command == 0:
    print('Ждём вас снова!')
    exit()


def sum_lines_columns(matrix):
    sum_lines = np.sum(matrix, axis=1)
    sum_columns = np.sum(matrix, axis=0)
    for i in range(len(sum_lines)):
        print(f'Сумма элементов строки {i + 1}: {sum_lines[i]}')
    for i in range(len(sum_columns)):
        print(f'Сумма элементов столбца {i + 1}: {sum_columns[i]}')


def main_secondary_diagonals(matrix):
    main_diagonal = np.diag(matrix)
    secondary_diagonal = np.diag(np.fliplr(matrix))
    print(f'Элементы главной диагонали: {main_diagonal}')
    print(f'Элементы побочной диагонали: {secondary_diagonal}')


def positive_above_main_diagonal(matrix):
    lines = matrix.shape[0]
    colums = matrix.shape[1]
    count_above_main_diagonal = 0
    for i in range(lines):
        for j in range(colums):
            if i < j and matrix[i, j] > 0:
                count_above_main_diagonal += 1
    return count_above_main_diagonal


def max_average(matrix):
    max_av = -float('inf')
    max_i = 0
    for i in range(len(matrix)):
        if float(np.mean(matrix[i])) > max_av:
            max_av = float(np.mean(matrix[i]))
            max_i = i
    print(f'Номер строки, для которой среднеарифметическое '
          f'значение ее элементов имеет максимальное значение: {max_i + 1}')


def positive_sum(matrix):
    total_sum = 0
    for i in range(len(matrix)):
        if all(x != 0 for x in matrix[i]):
            total_sum += sum(matrix[i][matrix[i] > 0])
    print(f'Сумма положительных элементов массива, '
          f'которые стоят в строках, не содержащих нулевых элементов: {total_sum}')


point_of_menu = int(input('''Меню функций:
1. Вычисление суммы элементов каждого столбца и строки
2. Вывод главной и побочной диагонали двумерного массива
3. Количество положительных элементов массива, расположенных выше главной диагонали
4. Номер строки, для которой среднеарифметическое значение ее элементов имеет максимальное значение
5. Вычисление суммы положительных элементов массива, которые стоят в строках, не содержащих нулевых элементов
0. Выйти из программы
'''))
while point_of_menu != 0:
    if point_of_menu == 1:
        sum_lines_columns(matrix)
    elif point_of_menu == 2:
        main_secondary_diagonals(matrix)
    elif point_of_menu == 3:
        print(f'Количество положительных элементов массива, '
              f'расположенных выше главной диагонали: {positive_above_main_diagonal(matrix)}')
    elif point_of_menu == 4:
        max_average(matrix)
    elif point_of_menu == 5:
        positive_sum(matrix)
    point_of_menu = int(input('''Меню функций:
1. Вычисление суммы элементов каждого столбца и строки
2. Вывод главной и побочной диагонали двумерного массива
3. Количество положительных элементов массива, расположенных выше главной диагонали
4. Номер строки, для которой среднеарифметическое значение ее элементов имеет максимальное значение
5. Вычисление суммы положительных элементов массива, которые стоят в строках, не содержащих нулевых элементов
0. Выйти из программы
'''))
if point_of_menu == 0:
    print('Ждём вас снова!')
    exit()
