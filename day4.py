from __future__ import print_function
import hashlib
prefix = 'yzbqklnj'

prefix_m = hashlib.md5(prefix)
def find_tail(startstring):
        
    tail = 0
    while True:
        curr_m = prefix_m.copy()
        curr_m.update(str(tail))
        md5_hash_hex = str(curr_m.hexdigest())
        if md5_hash_hex[:len(startstring)] == startstring:
            return tail
        tail += 1

print(find_tail('00000'))
print(find_tail('000000'))

