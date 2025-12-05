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

def extend_range(new_range,curr_ranges):
    for fresh_range in curr_ranges:
        if check_in_range(fresh_range, new_range[0]) and check_in_range(fresh_range, new_range[1]):
             return
        if check_in_range(fresh_range, new_range[0]):
             fresh_range[1] = new_range[1]
             return
        if check_in_range(fresh_range, new_range[1]):
             fresh_range[0] = new_range[0]
             return
    curr_ranges.append(new_range)

def check_in_range(fresh_range, id):
        return fresh_range[0] - id <= 0 and fresh_range[1] - id >= 0

def main(str_in):
    ranges = []
    comb_ranges = []
    ids = []
    ct = 0

    [str_ranges, str_ids] = str_in.split('\n\n')
    for str_range in str_ranges.split('\n'):
        ranges.append([int(str_range.split('-')[0]),int(str_range.split('-')[1])])
    
    ranges = sorted(ranges, key=lambda r: r[0])
    
    for id in str_ids.split('\n'):
        ids.append(int(id))
    
    for range in ranges:
         extend_range(range,comb_ranges)

    for fresh_range in comb_ranges:
         ct += (fresh_range[1] - fresh_range[0])+1
    
    return ct

print(main(real))