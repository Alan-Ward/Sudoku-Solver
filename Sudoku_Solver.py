matrix = [0,2,0,1,0,4,3,9,0,
          0,0,5,3,2,7,0,4,0,
          0,4,1,0,8,0,7,5,2,
          0,0,3,0,6,8,2,7,0,
          0,7,2,5,0,0,6,8,9,
          0,1,8,0,7,2,4,3,0,
          0,0,6,2,3,5,0,1,4,
          0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0]

def prettyPrint(m):
    
    for i in range(9):
        if i % 3 == 0:
            print("-------------")
        for j in range(9):
            if j % 3 == 0:
                print('|', end='')
            print(m[j+i*9], end='')
        print('|')
    print("-------------")


def vertical_check(matrix):
    for i in range(9):
        templist = [0,0,0,0,0,0,0,0,0]
        for j in range(9):
            templist[j] = matrix[(j*9)+i]
        for x in range(9):
            for y in range(9):
                if templist[x] == templist[y] and x != y and templist[x] > 0:
                    return False
    return True

def horizontal_check(matrix):
    for i in range(9):
        templist = [0,0,0,0,0,0,0,0,0]
        for j in range(9):
            templist[j] = matrix[(i*9)+j]
        for x in range(9):
            for y in range(9):
                if templist[x] == templist[y] and x != y and templist[x] > 0:
                    return False
    return True

def cube_check(matrix):
    for w in range(0,9,3):
        for x in range(0,9,3):
            templist = [0,0,0,0,0,0,0,0,0]
            for y in range(1,4):
                for z in range(1,4):
                    templist[(y+(z*3))-4] = matrix[((w*9)+x)+(y-1)+((z-1)*9)]
            for x in range(9):
                for y in range(9):
                    if templist[x] == templist[y] and x != y and templist[x] > 0:
                        return False
    return True

def all_check(matrix):
    if vertical_check(matrix) and horizontal_check(matrix) and cube_check(matrix):
        return True
    else:
        return False

def zero_count(matrix):
    return matrix.count(0)

def sudoku_solver(matrix):
    ### Sees if sudoku is solved ###
    if zero_count(matrix) == 0:   
        #print(matrix)
        return True
    else:

        ## finds first zero ##
        i = matrix.index(0)

        ## tries every different possible solution for the empty spot ##
        for j in range(1,10):
            matrix[i] = j

            ## if  potention solution works, run function with updated matrix ##
            if all_check(matrix):               
                if sudoku_solver(matrix):
                    return True
            ## if not, set index back to 0 (useful for when j = 9)
            matrix[i] = 0
    
    




sudoku_solver(matrix)
print(matrix)
prettyPrint(matrix)


#[8,2,7,1,5,4,3,9,6,
#9,6,5,3,2,7,1,4,8,
#3,4,1,6,8,9,7,5,2,
#5,9,3,4,6,8,2,7,1,
#4,7,2,5,1,3,6,8,9,
#6,1,8,0,7,2,4,3,5,
#7,8,6,2,3,5,9,1,4,
#1,5,4,7,9,6,8,2,3,
#2,3,9,8,4,1,5,6,7]