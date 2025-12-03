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

ct = 0
for bank in real.split('\n'):
    ct += get_joltage(bank)

print(ct)