from random import sample,randint
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
    '''
    0.0-2.2 0.3-2.5 0.6-2.8
    3.0-5.2 3.3-5.5 3.6-5.8
    6.0-8.2 6.3-8.5 6.6-8.8
    '''
    sq = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
    return sq[n]

def p_sq(n):
    start=f_sq(n)
    for r in range(3):
        for c in range(3):
            x = start[0]+r
            y = start[1]+c
            print(matrix[x,y],end='')
    print('\n')

def gen_sq():
    lst = list(range(1,10))
    return sample(lst,9)

def fill_sq(m,n,sq):
    start=f_sq(n)
    nu=0
    for r in range(3):
        for c in range(3):
            x = start[0]+r
            y = start[1]+c
            m[x][y]=sq[nu]
            nu+=1

def check_sq(m,n,sq):
    print("check: n={} sq={}".format(n,sq))
    return True

def main():
    print("Generate sudoku matrix")
    matrix = [ [0 for x in range(9)] for y in range(9) ]
    for square in range(0,9):
        seq=gen_sq()
        while check_sq(matrix,square,seq) is not True:
            seq=gen_sq()
        fill_sq(matrix,square,seq)
    p_matrix(matrix)

if __name__ == "__main__":
    main()

