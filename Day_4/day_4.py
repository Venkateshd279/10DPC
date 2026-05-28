# for loop 
# example 1
for i in range(100,101):
    print(i)

#output: 100

# example 2
for i in range(0,100):
    print(i)


#example 3
list = ['a','b',2,9,7.3]

for i in list:
    print(i)

# for loop in dictionary

dict = {"name": "venkatest", "age": 30, "city": "Chennai"}

for i in dict:
    print(i)

# two list convert into dictionary using for loop

list1 = ['name', 'age', 'city']
list2 = ['venkatesh', 30, 'Chennai']

dict = {}
for i in range(len(list1)):
    dict[list1[i]] = list2[i]
print(dict)