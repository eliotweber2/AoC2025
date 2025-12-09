import math

with open('P9/P9Input.txt') as f:
    real = f.read()

example = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''

def calc_largest_area(coords_lst):
    areas = []
    for i in range(len(coords_lst)-1):
        for j in range(i+1,len(coords_lst)):
            i_coord = coords_lst[i]
            j_coord = coords_lst[j]
            #print(i_coord, j_coord, abs(i_coord[0]-j_coord[0]) * abs(i_coord[1]-j_coord[1]))
            areas.append((abs(i_coord[0]-j_coord[0])+1) * (abs(i_coord[1]-j_coord[1])+1))
    
    return max(areas)

def parse(str_in):
    pts = []
    for line in str_in.split('\n'):
        pts.append([int(x) for x in line.split(',')])
    
    return pts

coords_lst = parse(real)

res = calc_largest_area(coords_lst)

print(res)