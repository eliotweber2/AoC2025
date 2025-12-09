import math
import numpy as np
import copy

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

def minify_coords(coords_lst):
    size_x = max([x[0] for x in coords_lst])
    size_y = max([x[1] for x in coords_lst])
    i = 0
    running_coords_lst = []
    new_x_coords = []
    for coord in coords_lst:
        coord.append(0)
        coord.append(0)
        running_coords_lst.append(coord)
    while i != size_x:
        '''
        temp_arr = np.zeros([15,15],dtype=str)
        temp_arr[temp_arr==''] = '.'
        for coord in new_x_coords:
            temp_arr[coord[0],coord[1]] = '#'
        for coord in running_coords_lst:
            temp_arr[coord[0],coord[1]] = '@'

        print(temp_arr)
        '''
        on_point = False
        if any([coord[0] == i for coord in coords_lst]):
            on_point = True
            i += 1
        else:
            size_x -= 1
        j = 0
        while j != len(running_coords_lst):
                coord = running_coords_lst[j]
                if coord[0] <= i:
                    running_coords_lst.remove(coord)
                    new_x_coords.append(coord)
                    continue
                else:
                    j += 1
                if not on_point:
                    coord[0] -= 1
                    coord[2] += 1
                        
    for coord in running_coords_lst:
        new_x_coords.append(coord)

    i = 0

    running_coords_lst = []
    new_y_coords = []
    for coord in new_x_coords:
        running_coords_lst.append(coord)

    print('a')

    while i != size_y:
        '''
        temp_arr = np.zeros([15,15],dtype=str)
        temp_arr[temp_arr==''] = '.'
        for coord in new_y_coords:
            temp_arr[coord[0],coord[1]] = '#'
        for coord in running_coords_lst:
            temp_arr[coord[0],coord[1]] = '@'

        print(temp_arr)
        '''
        on_point = False
        if any([coord[1] == i for coord in coords_lst]):
            on_point = True
            i += 1
        else:
            size_y -= 1
        j = 0
        while j != len(running_coords_lst):
                coord = running_coords_lst[j]
                if coord[1] <= i:
                    running_coords_lst.remove(coord)
                    new_y_coords.append(coord)
                    continue
                else:
                    j += 1
                if not on_point:
                    coord[1] -= 1
                    coord[3] += 1
                        
    for coord in running_coords_lst:
        new_y_coords.append(coord)

    print('b')
        
    return new_y_coords

def reorder(coords_lst,orig_lst):
    new_coords_lst = [0] * len(orig_lst)
    for new_coord in coords_lst:
        matching = [c for c in orig_lst
                     if new_coord[0] + new_coord[2] == c[0]
                     and new_coord[1] + new_coord[3] == c[1]
                    ][0]
        ind = orig_lst.index(matching)
        new_coords_lst[ind] = new_coord
    
    return new_coords_lst

def make_arr(coords_lst):
    size_x = max([x[0] for x in coords_lst])+3
    size_y = max([x[1] for x in coords_lst])+3
    arr = np.zeros([size_x,size_y],dtype=str)
    arr[arr == ''] = '.'
    for i in range(len(coords_lst)):
        if i == len(coords_lst)-1:
            coords_lst.append(coords_lst[0])
        #print(arr)
        if coords_lst[i][0] == coords_lst[i+1][0]:
            r = coords_lst[i][0]
            base_c = coords_lst[i][1]
            flip = coords_lst[i][1] > coords_lst[i+1][1]
            for c in range(abs(coords_lst[i][1]-coords_lst[i+1][1])+1):
                arr[r+1,base_c+c+1 if not flip else base_c-c+1] = "@"
        elif coords_lst[i][1] == coords_lst[i+1][1]:
            c = coords_lst[i][1]
            base_r = coords_lst[i][0]
            flip = coords_lst[i][0] > coords_lst[i+1][0]
            for r in range(abs(coords_lst[i][0]-coords_lst[i+1][0])+1):
                arr[base_r+r+1 if not flip else base_r-r+1,c+1] = "@"
        
        if i == len(coords_lst)-1:
            del[coords_lst[-1]]
    
    print(arr)
    return arr

def floodfill(arr):
    curr = [[0,0]]
    visited = []
    while len(curr) > 0:
        next_pt = curr.pop()
        arr[next_pt[0],next_pt[1]] = 'X'
        #print(arr)
        if next_pt[0] != 0:
            if [next_pt[0]-1,next_pt[1]] not in visited and arr[next_pt[0]-1,next_pt[1]] != '@' and arr[next_pt[0]-1,next_pt[1]] != 'X' and [next_pt[0]-1,next_pt[1]] not in curr:
                curr.append([next_pt[0]-1,next_pt[1]])
        if next_pt[1] != 0:
            if [next_pt[0],next_pt[1]-1] not in visited and arr[next_pt[0],next_pt[1]-1] != '@' and arr[next_pt[0],next_pt[1]-1] != 'X' and [next_pt[0],next_pt[1]-1] not in curr:
                curr.append([next_pt[0],next_pt[1]-1])
        if next_pt[0] != np.shape(arr)[0]-1:
            if [next_pt[0]+1,next_pt[1]] not in visited and arr[next_pt[0]+1,next_pt[1]] != '@' and arr[next_pt[0]+1,next_pt[1]] != 'X' and [next_pt[0]+1,next_pt[1]] not in curr:
                curr.append([next_pt[0]+1,next_pt[1]])
        if next_pt[1] != np.shape(arr)[0]-1:
            if [next_pt[0],next_pt[1]+1] not in visited and arr[next_pt[0],next_pt[1]+1] != '@' and arr[next_pt[0],next_pt[1]+1] != 'X' and [next_pt[0],next_pt[1]+1] not in curr:
                curr.append([next_pt[0],next_pt[1]+1])
    
    print(arr)

def calc_largest_area(coords_lst,arr):
    areas = []
    for i in range(len(coords_lst)-1):
        for j in range(i+1,len(coords_lst)):
            i_coord = coords_lst[i]
            j_coord = coords_lst[j]
            x_range = []
            y_range = []
            if i_coord[0] <= j_coord[0]:
                x_range = [i_coord[0],j_coord[0]+1]
            else:
                x_range = [j_coord[0],i_coord[0]+1]

            if i_coord[1] <= j_coord[1]:
                y_range = [i_coord[1],j_coord[1]+1]
            else:
                y_range = [j_coord[1],i_coord[1]+1]

            #print(i_coord,j_coord,x_range,y_range, 'X' in arr[x_range[0]:x_range[1],y_range[0]:y_range[1]])
            
            if 'X' in arr[x_range[0]:x_range[1],y_range[0]:y_range[1]]:
                continue
            
            #print(i_coord, j_coord, abs(i_coord[0]-j_coord[0]) * abs(i_coord[1]-j_coord[1]))
            areas.append((abs((i_coord[0]+i_coord[2])-(j_coord[0]+j_coord[2]))+1)
                          * (abs((i_coord[1]+i_coord[3])-(j_coord[1]+j_coord[3]))+1))
    
    print(areas)
    return max(areas)

def parse(str_in):
    pts = []
    for line in str_in.split('\n'):
        pts.append([int(x) for x in line.split(',')][::-1])
    
    return pts

coords_lst = parse(real)

new_lst = copy.deepcopy(coords_lst)

new_coords = reorder(minify_coords(new_lst),coords_lst)
'''
temp_arr = np.zeros([5,5],dtype=str)
temp_arr[temp_arr==''] = '.'
for coord in new_coords:
    temp_arr[coord[0],coord[1]] = '#'
for coord in new_coords:
    temp_arr[coord[0],coord[1]] = '@'

print(temp_arr)
'''
arr = make_arr(new_coords)

floodfill(arr)

arr = arr[1:np.shape(arr)[0]-1,1:np.shape(arr)[1]-1]
np.savetxt('P9/P9Output.txt',arr,fmt='%s')


res = calc_largest_area(new_coords,arr)

print(res)
