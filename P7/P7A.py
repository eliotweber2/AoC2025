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
        
def parse(str_in):
    return np.array([list(row) for row in str_in.split('\n')])

state_arr = parse(real)
state_arr[state_arr == 'S'] = '|'
final = get_final(state_arr)

print(final)