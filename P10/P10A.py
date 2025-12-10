from collections import deque
import copy

with open('P10/P10Input.txt') as f:
    real = f.read()

example = '''[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'''

def get_steps(goal,buttons):
    curr = deque()
    cache = set()
    for button in buttons:
        curr.append([button,0,[False]*len(goal)])
    
    while True:
        next_ele = curr.popleft()
        state = copy.deepcopy(next_ele[2])
        cache.add(''.join(['#' if x else '.' for x in state]))
        for light in next_ele[0]:
            state[light] = not next_ele[2][light]

        if ''.join(['#' if x else '.' for x in state]) in cache:
            continue
        
        if state == goal:
            print('hi')
            return next_ele[1]+1
        
        '''
        new_hist = []
        for x in next_ele[3]:
            new_hist.append(x)
        
        new_hist.append(next_ele[0])
        '''
        
        for button in buttons:
            curr.append([button,next_ele[1]+1,state])

def parse(str_in):
    states = []
    for line in str_in.split('\n'):
        items = line.split(' ')
        goal = [x == '#' for x in items[0]]
        buttons = items[1:-1]
        new_buttons = []
        for button in buttons:
            new_buttons.append([int(x) for x in button[1:-1].split(',')])
        
        states.append([goal[1:-1],new_buttons])
    
    return states

states = parse(real)
print(states)
tot = 0
for [goal,buttons] in states:
    res = get_steps(goal,buttons)
    tot += res
    print(goal,res)

print('tot ', tot)