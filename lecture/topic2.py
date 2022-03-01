
#Create a dictionary for grades
d = {'A':89, 'B':80, 'C':70, 'D': 60, 'G':-10}
print(str(d))

#whoops...G doesn't exist as a grade
if 'G' in d:
    del d['G']

#whoops also forgot f
d.update({'F':0})

#using same key overwrites...so we can 'correct' A
d.update({'A':90})

print(str(d['A']))
print(str(d.get('A')))

try:
    print(str(d.get('Z')))
except KeyError:
    print('Value is not in dictionary')

try:
    del d['Z']
except KeyError:
    print('Value is not in dictionary')

#get keys
keys_list = list(d)
print(str(keys_list))
values_list = d.values()
print(str(values_list))

tuple_pairs = d.items()
print(str(tuple_pairs))

#loop for both
for key, value in d.items():
    print(f'Key is "{key}" and value is "{value}"')

#loop for both
for key in d.keys():
    print(f'Key is "{key}" and value is "{d.get(key)}"')


