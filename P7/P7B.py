import numpy as np

with open('P7/P7Input.txt') as f:
    real = f.read()

example = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''

def get_final(state_arr):
    while True:
        final_ct = 0
        is_final = False
        beams = np.where(state_arr == '|')
       #print(state_arr)
        for beam in zip(*beams):
            if beam[0] == np.shape(state_arr)[0] - 1:
                is_final = True
                continue
            elif state_arr[beam[0]+1,beam[1]] == '|': continue
            elif state_arr[beam[0]+1,beam[1]] == '^':
                final_ct += 1
                state_arr[beam[0]+1,beam[1]+1] = '|'
                state_arr[beam[0]+1,beam[1]-1] = '|'
            elif state_arr[beam[0]+1,beam[1]] == '.':
                state_arr[beam[0]+1,beam[1]] = '|'

        if is_final:
            return final_ct
        
def get_col(arr,c):
    return arr[:,c]

def get_poss_splits(arr,r,c):
    if cache[r,c] != 0: return cache[r,c]
    if '^' not in get_col(arr,c-1)[r:] and '^' not in get_col(arr,c+1)[r:]:
        cache[r,c] = 2
        return 2
    side_1 = 1
    side_2 = 1
    if '^' in get_col(arr,c-1)[r:]:
        new_r = r + list(get_col(arr,c-1)[r:]).index('^')
        side_1 = get_poss_splits(arr,new_r,c-1)
    if '^' in get_col(arr,c+1)[r:]:
        new_r = r + list(get_col(arr,c+1)[r:]).index('^')
        side_2 = get_poss_splits(arr,new_r,c+1)

    #print(r,c,side_1+side_2)
    
    cache[r,c] = side_1+side_2

    return side_1 + side_2
        
def parse(str_in):
    return np.array([list(row) for row in str_in.split('\n')])

state_arr = parse(real)
'''
state_arr[state_arr == 'S'] = '|'
final = get_final(state_arr)
'''

#print(state_arr)

cache = np.zeros(np.shape(state_arr),dtype=int)

c = np.where(state_arr == 'S')[1][0]
#print(np.shape(state_arr))
final = get_poss_splits(state_arr,list(get_col(state_arr,c)).index('^'),c)

print(final)