# set operations 

# frozen set is immutable, it cannot be changed after creation
# we can create as unmutable set using frozenset() function

# example of set operations
# below are example of set
set1 = {1,2,3,4,5,6,7}
set2 = {4,5,6,7,8}

# important: set always contains unique values, it does not allow duplicates. 

common_elements = set1 & set2
print(common_elements)

combined_elements = set1 | set2
print(combined_elements)

frozen = frozenset(set1)
print(frozen)

# list of set operations
# union: set1 | set2
# intersection: set1 & set2
# difference: set1 - set2
difference = set1 - set2
print(difference)
# symmetric difference: set1 ^ set2
symmetric_difference = set1 ^ set2
print(symmetric_difference)




# frozen set operations with loop
frozen_set1 = frozenset({1,2,3,4,5})
frozen_set2 = frozenset({4,5,6,7,8})


for element in frozen_set1:
    print(element)

for element in frozen_set2:
    print(element)