import numpy as np

with open('P4/P4Input.txt') as f:
    real = f.read()

example = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''

def get_neighbor_ct(arr, i,j):
    ct = 0

    i_range = []
    j_range = []

    if i == 0:
        i_range = [0,2]
    elif i == arr.shape[0]-1:
        i_range = [arr.shape[0]-2,arr.shape[0]]
    else:
        i_range = [i-1,i+2]

    if j == 0:
        j_range = [0,2]
    elif j == arr.shape[1]-1:
        j_range = [arr.shape[1]-2,arr.shape[1]]
    else:
        j_range = [j-1,j+2]
    
    for n_i in range(*i_range):
        for n_j in range(*j_range):
            #print(n_i,n_j, arr[n_i,n_j])
            if arr[n_i,n_j] == '@' and (n_i != i or n_j != j):
                #print(n_i,n_j)
                ct += 1

    return ct

arr_input = [list(row) for row in real.split('\n')]
#print(arr_input)

arr = np.array(arr_input)

def main(arr):
    ct = 0

    for i in range(np.shape(arr)[0]):
        for j in range(np.shape(arr)[1]):
            if arr[i,j] == '@':
                #print(i,j,arr[i,j],get_neighbor_ct(arr,i,j))
                if get_neighbor_ct(arr,i,j) < 4:
                    
                    ct += 1

    print(ct)

main(arr)

#print(get_neighbor_ct(arr,0,7))