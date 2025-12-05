with open('P5/P5Input.txt') as f:
    real = f.read()

example = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''

def check_if_fresh(ranges, id):
    for fresh_range in ranges:
        if fresh_range[0] - id <= 0 and fresh_range[1] - id >= 0:
            return True
    
    return False

def main(str_in):
    ranges = []
    ids = []
    ct = 0

    [str_ranges, str_ids] = str_in.split('\n\n')
    for str_range in str_ranges.split('\n'):
        ranges.append([int(str_range.split('-')[0]),int(str_range.split('-')[1])])
    
    for id in str_ids.split('\n'):
        ids.append(int(id))
    
    for id in ids:
        if check_if_fresh(ranges, id): ct += 1
    
    return ct

print(main(real))