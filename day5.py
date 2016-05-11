from __future__ import print_function
import re

# first part
two = re.compile(r'.*(\w)\1+.*')
vovels = re.compile(r'.*[aeiou].*[aeiou].*[aeiou].*')
unwanted = re.compile(r'.*(ab|cd|pq|xy).*')

# second part
two_pairs = re.compile(r'.*(\w\w).*\1.*')
split_pair = re.compile(r'.*(\w).\1.*')

fname = './input_day5.txt'
with open(fname) as f:
    content = f.readlines()

content = [item.strip() for item in content]
dict_of_matches = {}
second_dict_of_matches = {}

for item in content:
    match = two.match(item) and vovels.match(item) and not unwanted.match(item)
    second_match = two_pairs.match(item) is not None and split_pair.match(item) is not None
    dict_of_matches.update({item : match})
    second_dict_of_matches.update({item : second_match})

print('Matches for the first part:')
print(dict_of_matches.values().count(True))
print('Matches for the second part:')
print(second_dict_of_matches.values().count(True))

