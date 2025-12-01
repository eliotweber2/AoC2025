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
    for rot in rot_lst:
        if rot[0] == "L":
            state -= rot[1]
            state += 100
        else:
            state += rot[1]
        state %= 100
        yield state

def parse(str_in):
    rot_lst = []
    for str_rot in str_in.splitlines():
        rot_lst.append([str_rot[0],int(str_rot[1:])])
    return rot_lst

def main(str_in):
    rot_lst = parse(str_in)
    ct = 0
    state_iter = state_generator(rot_lst)
    for state in list(state_iter):
        #print(state)
        if state == 0: ct += 1
    return ct

print(main(real))