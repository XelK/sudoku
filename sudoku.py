from random import sample,randint
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

def check_sq(matrix,sq,seq):
    start=f_sq(sq)
    x = start[0]
    y = start[1]
    rows = [ [0 for x in range(9)] for y in range(9) ]
    for i in range(9):
        rows[i]=[row[i] for row in matrix]
    #print("check| position: {}:{} seq: {} ".format(x,y,seq))
    for i in range(9):
        if i <3 and seq[i] in matrix[x] :
            return False
        if i>2 and i<6 and seq[i] in matrix[x+1]:
            return False
        if i>5 and seq[i] in matrix[x+2]:
            return False
    for i in range(9):
        if i==0 or i==3 or i==6:
            if seq[i] in rows[y]:
                return False
        if i==1 or i==4 or i==7 :
            if seq[i] in rows[y+1]:
                return False
        if i==2 or i==5 or i==8 : 
            if seq[i] in rows[y+2]:
                return False
    return True

def permut(matrix,sq):
    start=f_sq(sq)
    print(start)
    y = start[1]
    numbers=[[n for n in range(10) if n not in matrix[i]] for i in range(3) ]
    perms=[list(permutations(numbers[i])) for i in range(3)]
    print("all perms: ",perms)
    rows=[ [ matrix[r][c] for r in range(9)] for c in range(9) ]
    for i in range(3):
        for tup in perms[i]:
            pip=0
            for n in tup:
            #for n in range(3):
                print("{} from {} search in row {}:".format(n,tup,rows[y+pip]))
                if n in rows[y+pip]:
                    #print("****** REMOVE:  {}:".format(n))
                    perms[i].remove(tup)
                    break
                pip+=1
    return perms

def main():
    generated=0
    print("Generate sudoku matrix")
    matrix = [ [0 for x in range(9)] for y in range(9) ]
    for square in [0,4,8,2,6] : 
        seq=gen_sq()
        while check_sq(matrix,square,seq) is not True:
            seq=gen_sq()
        fill_sq(matrix,square,seq)
    p_matrix(matrix)
    print("perms: ",permut(matrix,1))

if __name__ == "__main__":
    main()
