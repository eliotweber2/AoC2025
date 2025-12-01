import math

example = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''

with open('P1/P1Input.txt') as f:
    real = f.read()

def state_generator(rot_lst):
    state = 50
    ct = 0
    for rot in rot_lst:
        #print(state, rot, ct)
        add_ct = False
        if rot[1] >= 100:
            ct += math.floor(rot[1] / 100)
            rot[1] %= 100
        if rot[0] == "L":
            prev = state
            state -= rot[1]
            if state < 0 and prev != 0:
                add_ct = True
                #print('b')
                ct += 1
            state += 100
        else:
            state += rot[1]
            if state > 100:
                add_ct = True
                #print('a')
                ct += 1
        state %= 100
        if state == 0 and not add_ct:
            #print('c')
            ct += 1
    return ct

def parse(str_in):
    rot_lst = []
    for str_rot in str_in.splitlines():
        rot_lst.append([str_rot[0],int(str_rot[1:])])
    return rot_lst

def main(str_in):
    rot_lst = parse(str_in)
    return state_generator(rot_lst)

print(main(real))