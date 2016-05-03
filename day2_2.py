from __future__ import print_function
from operator import mul

def get_surface_area(dims):
    return 2*dims[0]*dims[1] + 2*dims[1]*dims[2] + 2*dims[2]*dims[0]

def get_paper_need(dims):
    return dims[0] * dims[1] + get_surface_area(dims)

def get_smallest_perim(dims):
    return 2 * (dims[0] + dims[1])

def get_volume(dims):
    return reduce(mul, dims)

def get_ribbon_need(dims):
    return get_volume(dims) + get_smallest_perim(dims)

fname = './input_day2.txt'
with open(fname) as f:
    content = f.readlines()

# Strip trailing \n
content = [item.strip() for item in content]
split = [item.split('x') for item in content]
split = [[int(number) for number in dims] for dims in split]

for dims in split:
    dims.sort() 
    
need_list_paper = [get_paper_need(dims) for dims in split]
total_need_paper = sum(need_list_paper)

need_list_ribbon = [get_ribbon_need(dims) for dims in split]
total_need_ribbon = sum(need_list_ribbon)

print(total_need_paper)
print(total_need_ribbon)



