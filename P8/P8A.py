import numpy
import networkx as nx
import math

with open('P8/P8Input.txt') as f:
    real = f.read()

example = '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''

def get_distance(n1,n2):
    return math.sqrt(
        (n1[0]-n2[0])**2
        + (n1[1]-n2[1])**2
        + (n1[2]-n2[2])**2)

def parse(str_in):
    vecs = []
    for vec in str_in.split('\n'):
        vecs.append([int(x) for x in vec.split(',')])
    
    return vecs

def to_key(vec):
    return ','.join([str(x) for x in vec])

def main(vecs):
    name_dict = {}
    weights = {}
    ct = 0
    for i in vecs:
        name_dict[ct] = i
        ct += 1

    for i in vecs:
        for j in vecs:
            if i == j: continue
            weights[get_distance(i,j)] = [to_key(i),to_key(j)]

    nets = []
    G = nx.Graph()
    G.add_nodes_from([to_key(vec) for vec in vecs])

    dist_keys = sorted(list(weights.keys()),reverse=True)
    for i in range(1000):
        dist_key = dist_keys.pop()
        G.add_edge(*weights[dist_key], weight=dist_key)
    
    connected_subcomponents = nx.connected_components(G)

    disconnected_subgraphs = [G.subgraph(c) for c in connected_subcomponents]
    #print([graph.number_of_nodes() for graph in disconnected_subgraphs])
    return math.prod(sorted([graph.number_of_nodes() for graph in disconnected_subgraphs],reverse=True)[:3])

vecs = parse(real)

print(main(vecs))