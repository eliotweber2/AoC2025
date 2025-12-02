example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

with open('P2/P2Input.txt') as f:
    real = f.read()

def check_num(n):
    n = str(n)
    for i in range(1,int(len(n)/2)+1):
        test = n[0:i]
        if not len(n) % len(test) == 0: continue
        test *= int(len(n)/len(test))
        if n == test: return True
    
    return False

def check_num_simple(n):
    n = str(n)
    if len(n) % 2 != 0: return False
    return n[:int(len(n)/2)] == n[int(len(n)/2):len(n)]

def check_ranges(str_in):
    ct = 0
    str_ranges = str_in.split(',')
    for str_range in str_ranges:
        start, end = str_range.split('-')
        #print(int(end) - int(start))
        for n in range(int(start),int(end)+1):
            if check_num(n):
                #print(n)
                ct += n

    return ct

print(check_ranges(real))