from __future__ import print_function

def get_visited_houses(path_string):
    cord = [0,0]

    cord_set = {tuple(cord)}
    num_chars = len(path_string)
    for ii in range(0,num_chars):
        
        if path_string[ii] == '>':
            cord[0] += 1

        elif path_string[ii] == '<':
            cord[0] -= 1 

        elif path_string[ii] == '^':
            cord[1] += 1

        elif path_string[ii] == 'v':
            cord[1] -= 1

        cord_tuple = tuple(cord)
        cord_set.add(cord_tuple)

    return cord_set

fname = './input_day3.txt'
with open(fname) as f:
    content = f.readlines()

path_string = content[0]
odd_path = path_string[0::2]
even_path = path_string[1::2]

print('Total path')
print(len(get_visited_houses(path_string)))

print('Alternating path')
print(len(get_visited_houses(odd_path).union(get_visited_houses(even_path))))
