from collections import deque
import copy
import numpy as np
from scipy.optimize import linprog

with open('P10/P10Input.txt') as f:
    real = f.read()

example = '''[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'''

def get_steps(goal,buttons):
    curr = []
    cache = set()
    for button in buttons:
        curr.append([button,0,[0]*len(goal),{}])

    best = -1
    
    while len(curr) > 0:
        next_ele = curr.pop()
        
        if best > 0 and next_ele[1] >= best:
            continue
        state = copy.deepcopy(next_ele[2])
        cache.add(' '.join([str(x) for x in state]))
        valid = True
        for light in next_ele[0]:
            state[light] += 1
            if state[light] > goal[light]:
                valid = False
                break
        
        if not valid:
            continue

        if ' '.join([str(x) for x in state]) in cache:
            continue
        
        if state == goal:
            print('hi', best, len(curr))
            best = next_ele[1] + 1
            print(best)
        
        new_hist = {}
        for x in next_ele[3].items():
            new_hist[x[0]] = x[1]
        
        key = ' '.join([str(x) for x in button])
        if key in new_hist.keys():
            new_hist[key] += 1
        else:
            new_hist[key] = 1
        
        for button in buttons:
            for light in button:
                if state[light] == goal[light]: continue
            curr.append([button,next_ele[1]+1,state,new_hist])
    
    return best

def solve(goal,buttons):
    c = np.array([1] * len(buttons))

    A_eq = np.array(
        [[1 if i in button else 0 for button in buttons] for i in range(len(goal))]
    )

    b_eq = np.array(goal)

    bounds = [(0,None)] * len(buttons)

    integrality = np.ones_like(c,dtype=int)

    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds,integrality=integrality)
    return res.fun

def parse(str_in):
    states = []
    for line in str_in.split('\n'):
        items = line.split(' ')
        goal = items[-1]
        buttons = items[1:-1]
        new_buttons = []
        for button in buttons:
            new_buttons.append([int(x) for x in button[1:-1].split(',')])
        
        new_goal = [int(x) for x in goal[1:-1].split(',')]
        states.append([new_goal,new_buttons])
    
    return states

states = parse(real)
#print(states)
tot = 0
for [goal,buttons] in states:
    res = solve(goal,buttons)
    tot += res
    print(goal,res)

print('tot ', tot)