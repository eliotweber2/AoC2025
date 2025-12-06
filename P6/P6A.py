import math

with open('P6/P6Input.txt') as f:
    real = f.read()

example = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''

def parse(str_in):
    lines = [[x for x in line.split(' ') if x != ''] for line in str_in.split('\n')]
    eqs = []
    for i in range(len(lines[0])):
        eqs.append([lines[j][i] for j in range(len(lines))])
    
    return eqs

def solve(eq):
    op = eq.pop()
    eq = [int(i) for i in eq]
    if op == '*':
        return math.prod(eq)
    elif op == '+':
        return sum(eq)
    
def conv(eq,parity):
    nums = eq[:-1]
    spaced_nums = []
    new_nums = []
    places = max([len(i) for i in nums])
    for num in nums:
        #if len(num) == places: spaced_nums.append(num)
        needed = places - len(num)
        if parity: spaced_nums.append(' ' * needed + num)
        else: spaced_nums.append(num + ' ' * needed)
    for i in range(places):
        new_num = ''     
        for num in spaced_nums:
            new_num += num[i]
        new_nums.append(new_num)
    
    new_nums.append(eq[-1])

    return new_nums


eqs = parse(real)

tot = 0

#parity = True

for eq in eqs:
    #eq = conv(eq, parity)
    #parity = not parity
    #print(eq)
    tot += solve(eq)

print(tot)