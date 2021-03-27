'''
2048 Game

2048 is a game and you are expected to implement the move function for this game.
Arguments passed to the four functions is the matrix which we are using for 2048
The move function will be returning new matrix after moving the corresponding move.

Implement All The Four Moves Using These Functions -
1. move_up
2. move_down
3. move_left
4. move_right

Sample Input 1:
1 2 4 3 2 4 3 1 4

Sample Output 1:
[[4, 4, 2, 2], [0, 8, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 4, 0, 0], [4, 8, 2, 2]]
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 4], [0, 4, 8, 4]]
[[0, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0], [4, 8, 4, 0]]
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [8, 8, 4, 0]]
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 16, 4]]
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [16, 4, 0, 0]]
[[16, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
[[0, 0, 16, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
'''

import random
def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat

def merge(mat):
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
    
    return mat

def compress(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)
        
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                pos += 1
    
    return new_mat

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])
            
    return new_mat

def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    
    return new_mat

def move_up(grid):
    #Implement This Function
    transposed_grid = transpose(grid)
    new_grid = compress(transposed_grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    final_grid = transpose(new_grid)
    
    return final_grid

def move_down(grid):
    #Implement This Function
    transposed_grid = transpose(grid)
    reverse_grid = reverse(transposed_grid)
    new_grid = compress(reverse_grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid)
    
    return final_grid

def move_right(grid):
    #Implement This Function
    reverse_grid = reverse(grid)
    new_grid = compress(reverse_grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    final_grid = reverse(new_grid)
    
    return final_grid

def move_left(grid):
    #Implement This Function
    new_grid = compress(grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    
    return new_grid


mat = start_game()
mat[1][3] = 2
mat[2][2] = 2
mat[3][0] = 4
mat[3][1] = 8
mat[2][1] = 4
inputs = [int(ele) for ele in input().split()]
for ele in inputs:
    if ele == 1:
        mat = move_up(mat)
    elif ele == 2:
        mat = move_down(mat)
    elif ele == 3:
        mat = move_left(mat)
    else:
        mat = move_right(mat)
    print(mat)