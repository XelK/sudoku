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

#print(matrix)
def p_matrix(n):
    print("Matrix:")
    for l in range(9):
        print(n[l])

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

def fill_sq(n):
    lst = list(range(1,10))
    numbers = sample(lst,9)
    start=f_sq(n)
    nu=0
    for r in range(3):
        for c in range(3):
            x = start[0]+r
            y = start[1]+c
            matrix[x][y]=numbers[nu]
            nu+=1

def main():
    print("Generate sudoku graph")
    matrix = [ [0 for x in range(9)] for y in range(9) ]
    print("empty matrix:")
    p_matrix(matrix)
#matrix[0] = sample(lst,9)


if __name__ == "__main__":
    main()

