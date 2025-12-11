with open('P11/P11Input.txt') as f:
    real = f.read()

example = '''svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out'''

cache = {}

def get_all_paths(from_dict,node,tgt):
    if node == tgt:
        #print('hi')
        return 1
    
    if node not in list(from_dict.keys()):
        return 0
    
    if node in list(cache.keys()):
        #print('cache hit')
        return cache[node]

    paths = sum([get_all_paths(from_dict,new_node,tgt) for new_node in from_dict[node]])
    cache[node] = paths
    return paths

def parse(str_in):
    to_dict = {}
    from_dict = {}
    for line in str_in.split('\n'):
        from_node,to_nodes = line.split(': ')
        to_nodes_parsed = to_nodes.split(' ')
        if from_node in list(to_dict.keys()):
            to_dict[from_node] += to_nodes_parsed
        else:
            to_dict[from_node] = to_nodes_parsed

        for to_node in to_nodes_parsed:
            if to_node in list(from_dict.keys()):
                from_dict[to_node].append(from_node)
            else:
                from_dict[to_node] = [from_node]

    return to_dict,from_dict

to_dict,from_dict = parse(real)

out_dac = get_all_paths(from_dict,'out','dac')
cache = {}
dac_fft = get_all_paths(from_dict,'dac','fft')
cache = {}
fft_svr = get_all_paths(from_dict,'fft','svr')
path1 = out_dac*dac_fft*fft_svr

cache = {}
out_fft = get_all_paths(from_dict,'out','fft')
cache = {}
fft_dac = get_all_paths(from_dict,'fft','dac')
cache = {}
dac_svr = get_all_paths(from_dict,'dac','svr')
path2 = out_fft*fft_dac*dac_svr

print(path1+path2)