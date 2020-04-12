import random
from itertools import permutations
'''
matrix creation rules:
    every row: uniq numbers from 1 to 9
    every column: uniq numbers from 1 to 9
    every squares: uniq numbers from 1 to 9
        squares with coordinates:
        0.0-2.2 0.3-2.5 0.6-2.8
        3.0-5.2 3.3-5.5 3.6-5.8
        6.0-8.2 6.3-8.5 6.6-8.8
'''


def p_matrix(m):
    print("Matrix:")
    for l in range(9):
        print(m[l])


def f_sq(n):
    """
    0.0-2.2 0.3-2.5 0.6-2.8
    3.0-5.2 3.3-5.5 3.6-5.8
    6.0-8.2 6.3-8.5 6.6-8.8
    """
    sq = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
    return sq[n]


def p_sq(m, n):
    start = f_sq(n)
    for r in range(3):
        for c in range(3):
            x = start[0] + r
            y = start[1] + c
            print(m[x, y], end='')
    print('\n')


def gen_sq():
    lst = list(range(1, 10))
    return random.sample(lst, 9)


def fill_sq(m, n, sq):
    start = f_sq(n)
    nu = 0
    for r in range(3):
        for c in range(3):
            x = start[0] + r
            y = start[1] + c
            m[x][y] = sq[nu]
            nu += 1


def check_sq(m, sq, seq):
    start = f_sq(sq)
    x = start[0]
    y = start[1]
    rows = [[0 for x in range(9)] for y in range(9)]
    for i in range(9):
        rows[i] = [row[i] for row in m]
    # print("check| position: {}:{} seq: {} ".format(x,y,seq))
    for i in range(9):
        if i < 3 and seq[i] in m[x]:
            return False
        if 2 < i < 6 and seq[i] in m[x + 1]:
            return False
        if i > 5 and seq[i] in m[x + 2]:
            return False
    for i in range(9):
        if i == 0 or i == 3 or i == 6:
            if seq[i] in rows[y]:
                return False
        if i == 1 or i == 4 or i == 7:
            if seq[i] in rows[y + 1]:
                return False
        if i == 2 or i == 5 or i == 8:
            if seq[i] in rows[y + 2]:
                return False
    return True


def p_permut(m, sq):
    start = f_sq(sq)
    coordinates = [0, 3, 6, 0, 3, 6, 0, 3, 6]  # TODO: find better solution
    cs = coordinates[sq]
    y = start[1]
    numbers = [[n for n in range(10) if n not in m[i]] for i in range(3)]
    perms = [list(permutations(numbers[i])) for i in range(3)]
    columns = [[m[r][c] for r in range(9)] for c in range(9)]
    for p in perms:
        tup = 0
        while tup < len(p) - 1:
            number = 0
            while number < 3:
                if p[tup][number] in columns[cs + number]:
                    p.remove(p[tup])
                    tup = 0
                    break
                number += 1
            tup += 1
    return perms


def main():
    generated = 0
    print("Generate sudoku matrix")
    matrix = [[0 for x in range(9)] for y in range(9)]
    for square in [0, 2, 4, 6, 8]:
        seq = gen_sq()
        while check_sq(matrix, square, seq) is not True:
            seq = gen_sq()
        fill_sq(matrix, square, seq)
    p_matrix(matrix)
    perms = [p_permut(matrix, i) for i in [1, 3, 5, 7]]  # TODO: find better mode
    print("perms: ", perms)


if __name__ == "__main__":
    main()
