
#two ways to create sets
##set function
a_set = set('abcdddee')
print("a_set is: " + str(a_set))
##curly braces
another_set = {1,2,3,3,4,5,5,5,6}
print("another_set is: " + str(another_set))

#See python docs for more functions we can do with sets, but some examples

#add a value to a set
another_set.add(7)
print("another_set is: " + str(another_set))

#union sets
more_numbers = set([4,5,6,7,9,10])
union_set = another_set.union(more_numbers)
print('union is: ' + str(union_set))

#difference
difference = another_set.difference(more_numbers)
print('difference is: ' + str(difference))

#pop...just pulls a value out
popped_value = another_set.pop()
print('popped value is: ' + str(popped_value))
print('another set is: ' + str(another_set))

#length
print('lenth of set is: ' + str(len(another_set)))

#print each value
for letter in a_set:
    print(str(letter))

#conditional
print(str('a' in a_set))
print(str('z' in a_set))


#frozen sets
a_set = frozenset('abcdddee')
print("a_set is: " + str(a_set))

#immutible, so we can't change/modify
#this will throw an error
a_set.add('g')
