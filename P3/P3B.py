with open('P3/P3Input.txt') as f:
    real = f.read()

example = '''987654321111111
811111111111119
234234234234278
818181911112111'''

def get_joltage(bank):
    bank = [int(x) for x in list(bank)]
    first = max(bank[:-1])
    poss_i = [i for i,x in enumerate(bank) if x == first and i != len(bank)-1]
    complete = set()
    for i in poss_i:
        second = max(bank[i+1:])
        complete.add(int(str(first) + str(second)))
    
    return max(complete)

def get_poss(bank,left):
    #print(bank,left)
    if left == 1:
        return max(bank)
    
    max_val = max(bank[:-(left-1)])

    complete = set()
    
    for i in [i for i,x in enumerate(bank[:-(left-1)]) if x == max_val]:
        max_next = get_poss(bank[i+1:],left-1)
        complete.add(int(str(max_val) + str(max_next)))
    
    return max(complete)

ct = 0
for bank in real.split('\n'):
    res = get_poss(bank,12)
    #print(res)
    ct += res

print(ct)