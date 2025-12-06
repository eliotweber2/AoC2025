import math

with open('P6/P6Input.txt') as f:
    real = f.read()

example = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''

def parse(str_in):
    lines = str_in.split('\n')
    new_lines = []
    all_separators = []
    for line in lines[:-1]:
        separators = [-1]
        for i in range(1,len(line)-1):
            if line[i] == ' ' and line[i-1] != ' ': separators.append(i)
        separators.append(len(line))
        if all_separators == []:
            for x in separators:
                all_separators.append(x)
            continue
        for i in range(len(separators)):
            if separators[i] > all_separators[i]: all_separators[i] = separators[i]
    
    for line in lines:
        new_line = []
        for i in range(1, len(all_separators)):
            new_line.append(line[all_separators[i-1]+1:all_separators[i]])
        new_lines.append(new_line)
    eqs = []
    for i in range(len(new_lines[0])):
        eqs.append([new_lines[j][i] for j in range(len(new_lines))])
    
    return eqs

def solve(eq):
    op = eq.pop().replace(' ', '')
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

parity = True

for eq in eqs:
    eq = conv(eq, parity)
    parity = not parity
    #print(eq)
    tot += solve(eq)

print(tot)