import sys
from decimal import Decimal
from collections import defaultdict, Counter, OrderedDict
from math import log2

def I(E):
    return -log2(E)

def entropy(P_dist):
    out = 0
    for p_x in P_dist:
        out += (-p_x * log2(p_x))
    return out

def get_binary(string):
    return map(bin, bytearray(string))

def get_probability_distribution(d):
    n = sum(d.values())
    [d.update({k:Decimal((v/n)-v)})for k, v in d.items()]
    return d

def get_binary_dict(string, binary_string=False):
    if binary_string == False:
        grammar = string
    else:
        grammer = get_binary(string)
    return get_probability_distribution(Counter(grammar))

def get_binary_expansion(n):
    return 1/2**n

def get_bounds(d, symbol, lower = None, upper = None):
    if lower or upper == None:
        value_list = [v for v in d.values()]
        lower = sum(value_list[:list(d.keys()).index(symbol)])
        upper = sum(value_list[:list(d.keys()).index(symbol) + 1])
    elif list(d.keys()).index(symbol) != len(d.keys()):
        interval = upper - lower
        value_list = [(interval * v) for v in d.values()]
        lower = sum(value_list[:list(d.keys()).index(symbol)])
        upper = sum(value_list[:list(d.keys()).index(symbol) + 1])
    else:
        pass
    return lower, upper

def get_interval(encode_string):
    d = OrderedDict(get_binary_dict(encode_string))
    for count, i in enumerate(encode_string):
        if count == 0:
            lower, upper = get_bounds(d, i, lower = None, upper = None)
        else:
            lower, upper = get_bounds(d, i, lower = lower, upper = upper)
    return lower, upper

def get_compression(encode_string, l_bound = 0, u_bound = 1, out = [], i = 1):
    grammar = get_binary_dict(encode_string)
    lower, upper = get_interval(encode_string)
    print(out, lower, upper, l_bound, u_bound)
    if lower > get_binary_expansion(i):
        out.append(1)
        l_bound = get_binary_expansion(i)
        i += 1
        get_compression(encode_string, l_bound = l_bound, u_bound = u_bound, out = out, i = i)
    else:
        out.append(0)
        u_bound = get_binary_expansion(i)
        i += 1
        get_compression(encode_string, l_bound = l_bound, u_bound = u_bound, out = out, i = i)


#def decompress(binary_string):
#    binary_string = 
#    return NotImplementedError

if __name__ == "__main__":
    print("Running")
